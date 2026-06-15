import os

def ensure_reports_folder():
    os.makedirs("reports", exist_ok=True)