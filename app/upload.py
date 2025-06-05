import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

from storage3.exceptions import StorageApiError

def upload_resume(file_path, bucket_name="resumes"):
    file_name = os.path.basename(file_path)

    try:
        with open(file_path, "rb") as f:
            # Try to upload the file
            supabase.storage.from_(bucket_name).upload(file_name, f)
        print(f"✅ Uploaded {file_name}")
    except StorageApiError as e:
        # Handle already existing file (409 error)
        error_info = e.args[0] if e.args else {}
        if isinstance(error_info, dict) and error_info.get("statusCode") == 409:
            print(f"⚠️  File already exists: {file_name} — skipping upload")
        else:
            print(f"❌ Unexpected upload error: {e}")
            return None

    # In either case, return the public URL
    return f"{SUPABASE_URL}/storage/v1/object/public/{bucket_name}/{file_name}"
