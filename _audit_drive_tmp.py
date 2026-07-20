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

def list_in(fid, name):
    print(f"\n===== {name} ({fid}) =====")
    try:
        res = svc.files().list(
            q=f"'{fid}' in parents",
            corpora="drive", driveId=DRIVE_ID,
            includeItemsFromAllDrives=True, supportsAllDrives=True,
            pageSize=200, fields="files(id,name,mimeType)").execute()
        files = res.get("files", [])
        if not files:
            print("  (vacio)")
        for f in files:
            print(f"  {f['name']}  [{f['mimeType']}]  {f['id']}")
    except Exception as e:
        print(f"  [ERROR: {e}]")

print("=== Buscar README / Master Context ===")
res = svc.files().list(
    q="name contains 'README' or name contains 'Master' or name contains 'master'",
    corpora="drive", driveId=DRIVE_ID,
    includeItemsFromAllDrives=True, supportsAllDrives=True,
    pageSize=50, fields="files(id,name,mimeType,parents)").execute()
for f in res.get("files", []):
    print(f"  {f['name']} | {f['mimeType']} | {f['id']} | parents={f.get('parents')}")

print("\n=== RAIZ Shared Drive ===")
list_in(DRIVE_ID, "RAIZ")

print("\n=== Resources/Org ===")
list_in("1Entgs-rhgywtM_dMS2HStfBJAvKmq2-Y", "Resources/Org")
print("\n=== Areas/Legal & Compliance ===")
list_in("1u1u1xisg1cx8NrUXYIi71UY8A62UuIFx", "Areas/Legal")
print("\n=== Areas/Reviews ===")
list_in("1skIMJd5Qdw2VbdL_acZJJ5V3hSdt-xwF", "Areas/Reviews")
print("\n=== Resources/Templates ===")
list_in("1nDqtpaQ1dQiUMSax4ZmWsJmD5RdIG5p-", "Resources/Templates")
