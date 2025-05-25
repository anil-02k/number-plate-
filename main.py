from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import shutil
import uuid
import os
from detect_and_read import detect_and_read

app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    upload_dir = "temp_uploads"
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, f"{uuid.uuid4()}.jpg")

    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Run detection + OCR
    detected_text, confidence = detect_and_read(file_path)

    # Delete the file afterward
    os.remove(file_path)

    return JSONResponse(content={"number": detected_text, "confidence": confidence})
