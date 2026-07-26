import os
import urllib.request
import shutil

def download_file(url, folder, filename):
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.join(folder, filename)
    print(f"Downloading {url} to {path}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(path, 'wb') as out_file:
                out_file.write(response.read())
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

# High-fidelity realistic assets from HRA Organ Gallery (Raw GitHub links for stability)
hra_assets = {
    "brain": "https://raw.githubusercontent.com/cns-iu/hra-organ-gallery-in-vr/main/hra-organ-gallery/Assets/Models/Organs/lod-full%20v2.1/3d-allen-f-brain.glb",
    "heart": "https://raw.githubusercontent.com/cns-iu/hra-organ-gallery-in-vr/main/hra-organ-gallery/Assets/Models/Organs/lod-full%20v2.1/3d-vh-f-heart.glb",
    "kidney": "https://raw.githubusercontent.com/cns-iu/hra-organ-gallery-in-vr/main/hra-organ-gallery/Assets/Models/Organs/lod-full%20v2.1/3d-vh-f-kidney-l.glb",
    "lungs": "https://raw.githubusercontent.com/cns-iu/hra-organ-gallery-in-vr/main/hra-organ-gallery/Assets/Models/Organs/lod-full%20v2.1/3d-vh-f-lung-l.glb"
}

# Photorealistic Environment
env_assets = {
    "lab_bg": "https://live.staticflickr.com/342/32144577010_80d4a1b81a_o.jpg"
}

for name, url in hra_assets.items():
    download_file(url, "assets/v4/hra", f"{name}.glb")

for name, url in env_assets.items():
    download_file(url, "assets/v4/env", f"{name}.jpg")
