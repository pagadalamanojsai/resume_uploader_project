import os
import requests
from app.main import process_resume
from app.sheets_reader import fetch_resume_links

def download_pdf(url, dest_folder="data"):
    os.makedirs(dest_folder, exist_ok=True)
    filename = url.split("/")[-1]
    filepath = os.path.join(dest_folder, filename)

    response = requests.get(url)
    if response.status_code == 200:
        with open(filepath, "wb") as f:
            f.write(response.content)
        return filepath
    else:
        print(f"Failed to download: {url}")
        return None

def batch_process_from_sheet():
    df = fetch_resume_links()  # expects a "Resume" or "URL" column
    for _, row in df.iterrows():
        url = row.get("Resume") or row.get("URL")
        if not url:
            continue
        path = download_pdf(url)
        if path:
            process_resume(path)

if __name__ == "__main__":
    batch_process_from_sheet()
