import json, urllib.request
d = json.load(open('/opt/data/.plane_credentials.json'))
KEY = d['api_key']; BASE = d['base_url'].rstrip('/'); PID = d['project_id']
# estados
req = urllib.request.Request(f"{BASE}/api/v1/workspaces/nolvorn/projects/{PID}/issues/?page_size=200", headers={"X-API-Key": KEY})
data = json.load(urllib.request.urlopen(req, timeout=30))
results = data.get('results', [])
states = {}
for it in results:
    s = it.get('state','?')
    states[s] = states.get(s,0)+1
print("Estados (counts):", states)
# buscar workflow states
req2 = urllib.request.Request(f"{BASE}/api/v1/workspaces/nolvorn/projects/{PID}/states/", headers={"X-API-Key": KEY})
try:
    st = json.load(urllib.request.urlopen(req2, timeout=30))
    sr = st.get('results', st if isinstance(st,list) else [])
    print("Workflow states:")
    for s in sr:
        print("  ", s.get('name'), s.get('id'))
except Exception as e:
    print("states err:", e)
