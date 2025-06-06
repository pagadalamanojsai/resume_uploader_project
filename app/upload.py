import os
from supabase import create_client, Client
from dotenv import load_dotenv
from storage3.exceptions import StorageApiError

# Load environment variables from .env
load_dotenv()

# Get the Supabase URL and key from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Create the Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def upload_resume(file_path, bucket_name="resumes"):
    file_name = os.path.basename(file_path)

    try:
        with open(file_path, "rb") as f:
            # Try to upload the file
            response = supabase.storage.from_(bucket_name).upload(file_name, f)

            # Check if the upload was successful (no error)
            if response.error:
                print(f"❌ Upload failed: {response.error.message}")
                return None
            else:
                print(f"✅ Uploaded {file_name}")
    except StorageApiError as e:
        # Handle already existing file (409 error)
        error_info = e.args[0] if e.args else {}
        if isinstance(error_info, dict) and error_info.get("statusCode") == 409:
            print(f"⚠️  File already exists: {file_name} — skipping upload")
        else:
            print(f"❌ Unexpected upload error: {e}")
            return None

    # Return the public URL of the uploaded file
    return f"{SUPABASE_URL}/storage/v1/object/public/{bucket_name}/{file_name}"
