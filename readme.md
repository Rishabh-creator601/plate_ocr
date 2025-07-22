# 🚗 Number Plate Recognition & OCR

A **Streamlit-powered web app** that performs **automatic number plate detection** and **OCR (Optical Character Recognition)** using **YOLOv8** and **EasyOCR**.

🌐 **Live Demo:** [plateocr.streamlit.app](https://plateocr.streamlit.app)

---

## 🔍 Overview

This project combines **object detection** and **text recognition** to accurately detect vehicle number plates and extract alphanumeric text.

**Tech Stack:**

- 🧠 **YOLOv8 (Ultralytics)** for number plate detection  
- 👁️‍🗨️ **EasyOCR** for text extraction  
- 🚀 **Streamlit** for a responsive web UI

<p align="center">
  <img src="./media/demo_image.png" width="80%" alt="App Screenshot" />
</p>

---

## 🧠 Project Pipeline

```plaintext
Step 1: Input Image
    ↓
Step 2: YOLOv8 detects Number Plate
    ↓
Step 3: Crop Region of Interest (ROI)
    ↓
Step 4: EasyOCR extracts Text
    ↓
Step 5: Output — Plate Text + Confidence Score
