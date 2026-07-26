
import os
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def download_file(url, folder, filename):
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.join(folder, filename)
    print(f"Downloading {url} to {path}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx) as response:
            with open(path, 'wb') as out_file:
                out_file.write(response.read())
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

base_dir = r"C:\Users\anfyj\.gemini\antigravity\scratch\MedicardWebVR"
models_dir = os.path.join(base_dir, "assets", "v6", "models")
env_dir = os.path.join(base_dir, "assets", "v6", "env")

# Retry Lungs with jsdelivr
url_lungs = "https://cdn.jsdelivr.net/gh/cns-iu/hra-organ-gallery-in-vr@main/hra-organ-gallery/Assets/Models/Organs/lod-full%20v2.1/3d-vh-f-lung-l.glb"
download_file(url_lungs, models_dir, "lungs.glb")

# Alternate Sky
url_sky = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Equirectangular_projection_SW.jpg/1280px-Equirectangular_projection_SW.jpg"
download_file(url_sky, env_dir, "lab_sky.jpg")
