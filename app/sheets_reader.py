import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

def fetch_resume_links(sheet_name="testing", worksheet_index=0):
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets.readonly",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).get_worksheet(worksheet_index)
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    return df
