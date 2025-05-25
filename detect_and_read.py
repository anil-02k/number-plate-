import cv2
import torch
import easyocr
from ultralytics import YOLO

# Load YOLOv8 model (adjust if needed)
model = YOLO("runs/detect/train/weights/best.pt")
reader = easyocr.Reader(['en'], gpu=False)

def detect_and_read(image_path: str) -> tuple:
    try:
        results = model(image_path)
        img = cv2.imread(image_path)

        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cropped_img = img[y1:y2, x1:x2]

                ocr_result = reader.readtext(cropped_img)
                if ocr_result:
                    return ocr_result[0][1], float(ocr_result[0][2]) * 100  # Return text and confidence

        return "Number plate not detected", 0.0
    except Exception as e:
        return f"Error: {str(e)}", 0.0
