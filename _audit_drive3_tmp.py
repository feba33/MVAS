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
        f = svc.files().get(fileId=fid, fields="id,name,modifiedTime,version",
                            supportsAllDrives=True).execute()
        return f
    except Exception as e:
        return {"error": str(e)[:120]}

print("=== Master Context (Resources/Org 16Z) ===")
print(meta("16Z-nVVkWN7NW-yNVaidoD3kmtMO4ZC77kPEDnqP6XnM"))
print("\n=== nolvorn_master_context_v1 (raiz 11sUt) ===")
print(meta("11sUtS9K1bCs89BGtNy3G_lAuyPlUPLKab7aSOIzMxWM"))
print("\n=== Nolvorn Operations Tracker (1zCz) ===")
print(meta("1zC-z2MgKNy-X8UvJJY-_JJCVlfCcHG8bKMIAe7tzjXY"))

# Operations Tracker: list sheets/tabs
print("\n=== Operations Tracker tabs ===")
try:
    ss = svc.files().export_media(fileId="1zC-z2MgKNy-X8UvJJY-_JJCVlfCcHG8bKMIAe7tzjXY",
                                  mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet").execute()
    import io, zipfile
    z = zipfile.ZipFile(io.BytesIO(ss))
    # sheet names from workbook.xml
    wb = z.read("xl/workbook.xml").decode("utf-8")
    import re
    names = re.findall(r'<sheet[^>]*name="([^"]+)"', wb)
    print("TABS:", names)
except Exception as e:
    print("ERR:", str(e)[:200])
