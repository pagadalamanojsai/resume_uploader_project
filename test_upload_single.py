import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

assert SUPABASE_URL, "SUPABASE_URL is missing"
assert SUPABASE_KEY, "SUPABASE_KEY is missing"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

file_path = "data/akhilesh.21632.pdf"  # Pick any one file that exists
bucket_name = "resumes"
file_name = os.path.basename(file_path)

try:
    with open(file_path, "rb") as f:
        supabase.storage.from_(bucket_name).upload(file_name, f, upsert=True)

        print(f"✅ Successfully uploaded: {file_name}")
except Exception as e:
    print(f"❌ Upload failed:\n{e}")
