import os
import urllib.request

def download_file(url, folder, filename):
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.join(folder, filename)
    print(f"Downloading {url} to {path}...")
    try:
        # User agent to avoid blocks
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(path, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

# High-fidelity realistic assets from reliable Marketplaces
final_glbs = {
    "brain": "https://vazxmixjsiawhamurptp.supabase.co/storage/v1/object/public/models/brain/model.gltf", # I'll use GLTF for these if GLB fails
    "heart": "https://vazxmixjsiawhamurptp.supabase.co/storage/v1/object/public/models/heart/model.gltf",
    "lungs": "https://vazxmixjsiawhamurptp.supabase.co/storage/v1/object/public/models/lungs/model.gltf",
    "kidney": "https://vazxmixjsiawhamurptp.supabase.co/storage/v1/object/public/models/kidney/model.gltf"
}

# Actually, I'll use the ones that are KNOWN to be GLB
stable_glbs = {
    "heart": "https://cdn.jsdelivr.net/gh/pmndrs/market-assets@master/dist/heart.glb",
    "brain": "https://cdn.jsdelivr.net/gh/pmndrs/market-assets@master/dist/brain.glb",
    "skeleton": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Models/master/2.0/Box/glTF-Binary/Box.glb" # Placeholder
}

import shutil
for name, url in stable_glbs.items():
    download_file(url, "assets/v3", f"{name}.glb")
