from fastapi import FastAPI, UploadFile, File
import shutil
import os

app = FastAPI()

UPLOAD_DIR = os.getenv("STORAGE_DIR", "/data/images")

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}

