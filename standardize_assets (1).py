import os, shutil

base = r"C:\Users\anfyj\.gemini\antigravity\scratch\MedicardWebVR"
assets_dir = os.path.join(base, "assets")

# Organ to Keywords mapping
mapping = {
    'brain': ['brain'],
    'heart': ['heart'],
    'lungs': ['lung'],
    'skeleton': ['skeleton'],
    'kidney': ['kidney']
}

print("Standardizing assets...")

# Clean existing subfolders if they contain wrong filenames
for organ in mapping.keys():
    p = os.path.join(assets_dir, organ)
    if not os.path.exists(p): os.makedirs(p)

# Recursive search for models
for organ, keywords in mapping.items():
    found_fbx = None
    found_obj = None
    
    for root, dirs, files in os.walk(assets_dir):
        # Don't look inside our target folders to find sources
        if any(os.path.join(assets_dir, o) == root for o in mapping.keys()):
            continue
            
        for f in files:
            fl = f.lower()
            if any(k in fl for k in keywords):
                if fl.endswith('.fbx') and not found_fbx:
                    found_fbx = os.path.join(root, f)
                elif fl.endswith('.obj') and not found_obj:
                    found_obj = os.path.join(root, f)
    
    # Prioritize FBX
    best_model = found_fbx if found_fbx else found_obj
    if best_model:
        ext = os.path.splitext(best_model)[1].lower()
        target_path = os.path.join(assets_dir, organ, organ + ext)
        print(f"Copying {organ}: {best_model} -> {target_path}")
        shutil.copy2(best_model, target_path)
        
        # Copy textures from the source directory
        src_dir = os.path.dirname(best_model)
        for f in os.listdir(src_dir):
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.tga')):
                shutil.copy2(os.path.join(src_dir, f), os.path.join(assets_dir, organ))

print("Standardization complete.")
