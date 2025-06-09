import os
from supabase import create_client, Client
from dotenv import load_dotenv
from storage3.exceptions import StorageApiError

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

print("✅ Supabase URL loaded as:", SUPABASE_URL)
print("✅ Supabase Key loaded:", SUPABASE_KEY[:10], "...")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("❌ Missing SUPABASE_URL or SUPABASE_KEY in .env file")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def upload_resume(file_path, bucket_name="resumes"):
    file_name = os.path.basename(file_path)

    try:
        with open(file_path, "rb") as f:
            response = supabase.storage.from_(bucket_name).upload(file_name, f)

            if hasattr(response, "error") and response.error:
                print(f"❌ Upload failed: {response.error.message}")
                return None
            else:
                print(f"✅ Uploaded {file_name}")
    except StorageApiError as e:
        error_info = e.args[0] if e.args else {}
        if isinstance(error_info, dict) and error_info.get("statusCode") == 409:
            print(f"⚠️ File already exists: {file_name} — skipping upload")
        else:
            print(f"❌ Unexpected upload error: {e}")
            return None
    except Exception as e:
        print(f"❌ General error during upload: {e}")
        return None

    return f"{SUPABASE_URL}/storage/v1/object/public/{bucket_name}/{file_name}"
