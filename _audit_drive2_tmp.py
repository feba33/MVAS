import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

TK = "/opt/data/google_token.json"
DRIVE_ID = "0ADXc9xJB9XxQUk9PVA"
creds = Credentials.from_authorized_user_file(TK, ["https://www.googleapis.com/auth/drive"])
if creds.expired and creds.refresh_token:
    creds.refresh(Request())
svc = build("drive", "v3", credentials=creds)

def meta(fid):
    try:
        f = svc.files().get(fileId=fid, fields="id,name,modifiedTime,version,owners").execute()
        return f
    except Exception as e:
        return {"error": str(e)}

def export(fid, n=3000):
    try:
        data = svc.files().export_media(fileId=fid, mimeType="text/plain").execute()
        return data.decode("utf-8", errors="replace")[:n]
    except Exception as e:
        return f"[ERR {e}]"

print("=== METADATA Master Context (Resources/Org 16Z) ===")
print(meta("16Z-nVVkWN7NW-yNVaidoD3kmtMO4ZC77kPEDnqP6XnM"))
print("\n=== METADATA nolvorn_master_context_v1 (raiz 11sUt) ===")
print(meta("11sUtS9K1bCs89BGtNy3G_lAuyPlUPLKab7aSOIzMxWM"))

print("\n=== README (raiz 10ZWH8S) ===")
print(export("10ZWH8S-Zd-VaglHQMqT5EWYdNnfIrUeJd-NfDJFwtLE", 5000))

print("\n=== Nolvorn Operations Tracker metadata ===")
print(meta("1zC-z2MgKNy-X8UvJJY-_JJCVlfCcHG8bKMIAe7tzjXY"))
