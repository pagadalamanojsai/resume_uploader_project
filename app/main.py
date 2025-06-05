from app.upload import upload_resume
from app.extract import extract_text_from_pdf, extract_resume_data
from app.database import store_metadata_in_db

def process_resume(path):
    file_url = upload_resume(path)
    if not file_url:
        return
    text = extract_text_from_pdf(path)
    info = extract_resume_data(text)
    store_metadata_in_db(info, file_url)
