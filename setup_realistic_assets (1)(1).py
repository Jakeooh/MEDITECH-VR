
import os
import urllib.request
import ssl

# Ignore SSL certificate errors
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

# High-fidelity realistic assets from HRA Organ Gallery
hra_assets = {
    "brain": "https://cdn.jsdelivr.net/gh/cns-iu/hra-organ-gallery-in-vr@main/hra-organ-gallery/Assets/Models/Organs/lod-full%20v2.1/3d-allen-f-brain.glb",
    "heart": "https://cdn.jsdelivr.net/gh/cns-iu/hra-organ-gallery-in-vr@main/hra-organ-gallery/Assets/Models/Organs/lod-full%20v2.1/3d-vh-f-heart.glb",
    # "kidney": "https://cdn.jsdelivr.net/gh/cns-iu/hra-organ-gallery-in-vr@main/hra-organ-gallery/Assets/Models/Organs/lod-full%20v2.1/3d-vh-f-kidney-l.glb",
    # Using raw content for Kidney/Lungs if jsdelivr is cached/stale or failing
    "kidney": "https://raw.githubusercontent.com/cns-iu/hra-organ-gallery-in-vr/main/hra-organ-gallery/Assets/Models/Organs/lod-full%20v2.1/3d-vh-f-kidney-l.glb",
    "lungs": "https://raw.githubusercontent.com/cns-iu/hra-organ-gallery-in-vr/main/hra-organ-gallery/Assets/Models/Organs/lod-full%20v2.1/3d-vh-f-lung-l.glb"
}

# Environment
env_assets = {
    "lab_sky": "https://cdn.jsdelivr.net/gh/mrdoob/three.js@master/examples/textures/2294472375_bcf447ee1a_b.jpg"
}

base_dir = r"C:\Users\anfyj\.gemini\antigravity\scratch\MedicardWebVR"
models_dir = os.path.join(base_dir, "assets", "v6", "models")
env_dir = os.path.join(base_dir, "assets", "v6", "env")

for name, url in hra_assets.items():
    download_file(url, models_dir, f"{name}.glb")

for name, url in env_assets.items():
    download_file(url, env_dir, f"{name}.jpg")

print("Download complete.")
