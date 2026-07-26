import os

base_dir = r"C:\Users\anfyj\.gemini\antigravity\scratch\MedicardWebVR\assets"
folders = ['brain', 'heart', 'lungs', 'kidney', 'skeleton']

for folder in folders:
    p = os.path.join(base_dir, folder)
    if os.path.exists(p):
        files = os.listdir(p)
        print(f"[{folder}]")
        for f in files:
            if f.startswith("model"):
                size = os.path.getsize(os.path.join(p, f))
                print(f"  {f} ({size} bytes)")
    else:
        print(f"[{folder}] - FOLDER MISSING")
