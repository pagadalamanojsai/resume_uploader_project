from app.upload import upload_resume
from app.extract import extract_text_from_pdf, extract_resume_data
from app.database import store_metadata_in_db

def process_resume(file_path):
    print(f"\n📄 Processing: {file_path}")
    text = extract_text_from_pdf(file_path)

    info = extract_resume_data(text)
    print("🧠 Extracted Info:", info)

    file_url = upload_resume(file_path)
    print("📎 Uploaded File URL:", file_url)

    store_metadata_in_db(info, file_url)
