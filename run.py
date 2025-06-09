import os
print("🔎 DEBUG: SUPABASE_URL =", os.getenv("SUPABASE_URL"))
print("🔎 DEBUG: SUPABASE_KEY =", os.getenv("SUPABASE_KEY")[:10], "...")


from dotenv import load_dotenv
load_dotenv()

# Then run the batch_process directly (no subprocess needed)
from app.batch_process import batch_process_from_sheet

if __name__ == "__main__":
    batch_process_from_sheet()
