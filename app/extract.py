import spacy
import pdfplumber

nlp = spacy.load("en_core_web_sm")  # ✅ REQUIRED

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''.join([page.extract_text() or "" for page in pdf.pages])
    return text

def extract_resume_data(text):
    doc = nlp(text)
    name = doc.ents[0].text if doc.ents else "Unknown"
    email = next((token.text for token in doc if token.like_email), "unknown@example.com")
    phone = next((token.text for token in doc if token.like_num and len(token.text) >= 10), "0000000000")
    skills = [ent.text for ent in doc.ents if ent.label_ == "SKILL"]
    return {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills
    }
