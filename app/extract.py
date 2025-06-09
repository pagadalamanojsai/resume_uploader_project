import spacy
import pdfplumber
from pdf2image import convert_from_path
import pytesseract

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    text = extract_text_with_pdfplumber(pdf_path)

    if not text.strip():  # fallback if no text or garbage
        print("⚠️ PDF text extraction failed. Falling back to OCR...")
        text = ocr_extract_text_from_pdf(pdf_path)

    return text

def extract_text_with_pdfplumber(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            return ''.join([page.extract_text() or "" for page in pdf.pages])
    except Exception as e:
        print(f"❌ pdfplumber error: {e}")
        return ""

def ocr_extract_text_from_pdf(pdf_path):
    try:
        images = convert_from_path(pdf_path)
        text = ""
        for page_image in images:
            text += pytesseract.image_to_string(page_image)
        return text
    except Exception as e:
        print(f"❌ OCR failed: {e}")
        return ""

def extract_resume_data(text):
    doc = nlp(text)
    name = doc.ents[0].text if doc.ents else "Unknown"
    email = next((token.text for token in doc if token.like_email), "unknown@example.com")
    phone = next((token.text for token in doc if token.like_num and len(token.text) >= 10), "0000000000")
    
    # Set default empty list to avoid NameError
    skills = [ent.text for ent in doc.ents if ent.label_ == "SKILL"] if doc.ents else []

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills
    }
