from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

print("✅ Supabase URL loaded as:", SUPABASE_URL)
print("✅ Supabase Key loaded:", SUPABASE_KEY[:10], "...")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def store_metadata_in_db(data, file_url):
    skills_str = ", ".join(data["skills"]) if isinstance(data["skills"], list) else data["skills"]

    metadata = {
        "name": data.get("name", ""),
        "email": data.get("email", ""),
        "phone": data.get("phone", ""),
        "skills": skills_str,
        "file_url": file_url
    }

    try:
        response = supabase.table("resumes_metadata").insert(metadata).execute()
        print("📦 Metadata inserted successfully:", response)
    except Exception as e:
        print("❌ Database insert error:", e)
