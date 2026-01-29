import os

def check_images(folder):
    """Simple validator to check if files exist for the OCR pipeline."""
    if not os.path.exists(folder):
        print("Folder missing.")
        return
    
    files = os.listdir(folder)
    print(f"VisionSync Scan: Found {len(files)} files.")
    for f in files:
        if f.endswith(('.jpg', '.png', '.jpeg')):
            print(f"[READY] {f}")
        else:
            print(f"[SKIP] {f}")

if __name__ == "__main__":
    check_images("inputs")
"""
Module: shadow_archive.py
Objective: Automate the sorting of downloads into specialized vault sectors.
"""

import os
import shutil
from pathlib import Path

# --- TARGET DIRECTORIES ---
DOWNLOADS_PATH = Path.home() / "Downloads"
VAULT_BASE = Path.home() / "SYSTEM_VAULT_2026"

# Mapping: Extension -> Vault Sector
DIRECTORIES = {
    "CODE": [".py", ".ipynb", ".sql", ".js", ".java"],
    "DOCS": [".pdf", ".docx", ".txt", ".csv"],
    "MEDIA": [".jpg", ".jpeg", ".png", ".mp4"],
    "ARCHIVES": [".zip", ".rar", ".tar"]
}

def organize_vault():
    # 1. Initialize Vault Sectors
    for sector in DIRECTORIES.keys():
        (VAULT_BASE / sector).mkdir(parents=True, exist_ok=True)

    # 2. Sweep Downloads
    print(f"[*] Scanning {DOWNLOADS_PATH} for deployment...")
    
    for item in DOWNLOADS_PATH.iterdir():
        if item.is_dir(): continue
        
        # Check extension against mapping
        for sector, extensions in DIRECTORIES.items():
            if item.suffix.lower() in extensions:
                dest = VAULT_BASE / sector / item.name
                print(f"[+] Archiving {item.name} -> {sector}")
                shutil.move(str(item), str(dest))
                break

if __name__ == "__main__":
    try:
        organize_vault()
        print("\n[!] Vault Architecture Optimized.")
    except Exception as e:
        print(f"[X] System Error: {e}")
