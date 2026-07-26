import os, shutil

base = r"C:\Users\anfyj\.gemini\antigravity\scratch\MedicardWebVR"
assets_dir = os.path.join(base, "assets")

# Target folders
mapping = {
    'brain': ['brain'],
    'heart': ['heart'],
    'lungs': ['lungs', 'lungh'],
    'skeleton': ['skeleton'],
    'kidney': ['kidney']
}

print("Searching for models in nested structure...")
for organ, keywords in mapping.items():
    dest_dir = os.path.join(assets_dir, organ)
    if not os.path.exists(dest_dir): os.makedirs(dest_dir)
    
    found = False
    for root, dirs, files in os.walk(assets_dir):
        # Skip if already in the target subfolder to avoid infinite copy
        if root == dest_dir: continue
        
        for file in files:
            fl = file.lower()
            if any(k in fl for k in keywords) and (fl.endswith('.fbx') or fl.endswith('.obj')):
                src_path = os.path.join(root, file)
                ext = os.path.splitext(fl)[1].lower()
                dest_path = os.path.join(dest_dir, "model" + ext)
                
                print(f"Found {organ}: {src_path} -> {dest_path}")
                shutil.copy2(src_path, dest_path)
                
                # Copy textures from same dir
                for tex in files:
                    if any(tex.lower().endswith(e) for e in ['.png', '.jpg', '.jpeg', '.tga']):
                        try:
                            shutil.copy2(os.path.join(root, tex), dest_dir)
                        except:
                            pass # File might be busy
                
                found = True
                break
        if found: break

# Clean up root files
for f in os.listdir(assets_dir):
    p = os.path.join(assets_dir, f)
    if os.path.isfile(p) and f.lower().endswith(('.obj', '.fbx', '.zip')):
        try:
            os.remove(p)
        except:
            pass

print("Reorganization complete.")
