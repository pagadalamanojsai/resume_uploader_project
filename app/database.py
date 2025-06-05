from app.upload import supabase

def store_metadata_in_db(data, file_url):
    metadata = {
        "name": data.get("name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "skills": ', '.join(data.get("skills", [])),
        "file_url": file_url
    }

    print("📦 Metadata to insert:", metadata)  # 👈 Add this line

    response = supabase.table("resumes_metadata").insert(metadata).execute()
    print("✅ Metadata stored:", response)


