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

# Ultra-optimized, web-ready assets (<2MB)
optimized_assets = {
    "brain": "https://cdn.jsdelivr.net/gh/pmndrs/market-assets@master/dist/brain.glb",
    "heart": "https://cdn.jsdelivr.net/gh/pmndrs/market-assets@master/dist/heart.glb",
    "lab_bg": "https://cdn.jsdelivr.net/gh/mrdoob/three.js@master/examples/textures/2294472375_bcf447ee1a_b.jpg" # Standard Three.js equirect panorama (~500KB)
}

# Lungs and Kidney are a bit harder to find in direct raw CDN. 
# I will use high-quality primitives with textures or find another source.
# For now, let's get the core ones.

for name, url in optimized_assets.items():
    if "bg" in name:
        download_file(url, "assets/v6/env", f"{name}.jpg")
    else:
        download_file(url, "assets/v6/models", f"{name}.glb")
