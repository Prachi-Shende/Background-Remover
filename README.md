# Background Remover with OpenCV and SelfiSegmentation

A real-time background remover using OpenCV and the `SelfiSegmentation` module from `cvzone`. The system removes the webcam background and replaces it with custom images, enabling users to switch between them interactively.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-RealTime-green)
![cvzone](https://img.shields.io/badge/cvzone-SelfiSegmentation-blue)

---

- Replaces webcam background in real-time
- Cycle through different background images using keyboard keys
- Displays real-time FPS

---

## Features

- Real-time background removal using `SelfiSegmentation`
- Easily switch between multiple custom backgrounds
- Adjustable threshold for segmentation quality
- Stacked preview of original and background-removed frames
- Real-time FPS display

---

## Project Structure

BackgroundRemoverProject/  
├── images/ — Folder containing background images (resized to 640x480)  
├── background_remover.py — Main script for real-time background replacement  
├── requirements.txt — Python dependencies  
└── README.md — This documentation

---

## Tech Stack

| Library      | Use Case                               |
|--------------|----------------------------------------|
| OpenCV       | Video capture and image manipulation   |
| cvzone       | SelfiSegmentation module for background removal |
| NumPy        | Image array operations (via OpenCV)    |
| os           | File system operations for loading images |

---

## Setup Instructions

1. Clone the repository  
   ```bash
   git clone https://github.com/YourUsername/BackgroundRemoverProject.git
   cd BackgroundRemoverProject
   ```

2. Create and activate a virtual environment  
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # Windows
   ```

3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

4. Add background images  
   - Place images inside the `images/` directory.
   - Make sure each image is `640x480` or will be auto-resized.

5. Run the project  
   ```bash
   python background_remover.py
   ```

---

## Controls

| Key | Action                     |
|-----|----------------------------|
| `a` | Previous background image  |
| `d` | Next background image      |
| `q` | Quit the application       |

---

## requirements.txt

```txt
opencv-python
cvzone
numpy
```

---

## How It Works

- Captures live webcam feed using OpenCV.
- Uses `SelfiSegmentation` from `cvzone` to remove the background.
- Loads all images from the `images/` folder and allows cycling through them.
- Displays the original and processed frames side-by-side using `cvzone.stackImages`.

---

## Notes

- Works best with good lighting and clear background contrast.
- All background images should be the same size (preferably 640x480).
- `cvzone` internally uses MediaPipe's segmentation models.

---

## Credits

- [cvzone](https://github.com/cvzone/cvzone)
- [OpenCV](https://opencv.org/)

---

## Feedback

Feel free to fork, improve, and raise issues in the repository.
