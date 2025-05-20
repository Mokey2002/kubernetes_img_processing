import os
import time
from PIL import Image

STORAGE_DIR = os.getenv("STORAGE_DIR", "/data/images")
PROCESSED_DIR = os.path.join(STORAGE_DIR, "processed")
os.makedirs(PROCESSED_DIR, exist_ok=True)

def process_image(file_path):
    img = Image.open(file_path)
    img = img.resize((300, 300))
    processed_path = os.path.join(PROCESSED_DIR, os.path.basename(file_path))
    img.save(processed_path)

if __name__ == "__main__":
    while True:
        for fname in os.listdir(STORAGE_DIR):
            if fname.endswith(".jpg") and not os.path.exists(os.path.join(PROCESSED_DIR, fname)):
                process_image(os.path.join(STORAGE_DIR, fname))
        time.sleep(5)

