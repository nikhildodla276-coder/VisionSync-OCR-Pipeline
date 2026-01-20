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
