# Smart License Plate Recognition

This project is a smart license plate recognition system that uses advanced computer vision and machine learning techniques to detect and read vehicle license plates from images.

## Features

- Object detection using YOLOv8 model for license plate localization
- Optical Character Recognition (OCR) using EasyOCR to read license plate text
- FastAPI backend providing a REST API endpoint for predictions
- Streamlit frontend for easy image upload and result visualization
- Confidence scoring for OCR results
- Supports multiple image input methods (upload or camera capture)

## Project Structure

- `main.py`: FastAPI backend application exposing `/predict` endpoint for license plate recognition.
- `detect_and_read.py`: Core detection and OCR logic using YOLOv8 and EasyOCR.
- `app.py`: Streamlit frontend application for user interaction.
- `split_dataset.py`: (Assumed) script for dataset splitting (train/test).
- `data.yaml`: Dataset configuration file.
- `runs/detect/train/weights/best.pt`: Trained YOLOv8 model weights.
- `images/`: Sample vehicle images used for testing or training.
- `labels/`: Corresponding labels for images.
- `requirements.txt`: Python dependencies.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/anil-02k/number-plate-.git
   cd number-plate-
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run the FastAPI Backend

```bash
uvicorn main:app --reload
```

This will start the backend server at `http://localhost:8000`.

### Run the Streamlit Frontend

In a separate terminal, run:

```bash
streamlit run app.py
```

This will open the web interface where you can upload vehicle images or take photos for license plate recognition.

### API Endpoint

- `POST /predict`: Accepts an image file and returns the detected license plate number and confidence score.

Example response:

```json
{
  "number": "ABC1234",
  "confidence": 95.6
}
```

## Technical Details

- The YOLOv8 model is trained to detect license plates in vehicle images.
- Detected license plate regions are cropped and passed to EasyOCR for text recognition.
- The system returns the recognized text along with a confidence percentage.
- The Streamlit app interacts with the FastAPI backend via HTTP requests.

## Applications

- Parking management systems
- Traffic monitoring
- Security and surveillance
- Toll collection automation

## License

Specify your license here.

## Acknowledgments

- YOLOv8 by Ultralytics
- EasyOCR for optical character recognition
- FastAPI for backend API
- Streamlit for frontend UI
