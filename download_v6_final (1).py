import os
import urllib.request

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

# Finding a small, reliable 360 panorama (~1MB)
assets_v6 = {
    "brain": "https://cdn.jsdelivr.net/gh/pmndrs/market-assets@master/dist/brain.glb",
    "heart": "https://cdn.jsdelivr.net/gh/pmndrs/market-assets@master/dist/heart.glb",
    "lab_sky": "https://cdn.jsdelivr.net/gh/mrdoob/three.js@master/examples/textures/2294472375_bcf447ee1a_b.jpg"
}

for name, url in assets_v6.items():
    folder = "assets/v6/models" if name != "lab_sky" else "assets/v6/env"
    ext = ".glb" if name != "lab_sky" else ".jpg"
    download_file(url, folder, f"{name}{ext}")
