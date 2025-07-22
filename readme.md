# 🚗 Number Plate Recognition & OCR

A **Streamlit-powered web app** that performs **automatic number plate detection** and **OCR (Optical Character Recognition)** using **YOLOv8** and **EasyOCR**.

🌐 **Live Demo:** [plateocr.streamlit.app](https://plateocr.streamlit.app)

---

## 🔍 Overview

This project combines **object detection** and **text recognition** to accurately identify vehicle number plates and extract alphanumeric text from them.

Built using:

- 🧠 YOLOv11 (Ultralytics) for number plate detection  
- 👁️‍🗨️ EasyOCR for recognizing characters  
- 🚀 Streamlit for UI  

---

## 🧠 Project Pipeline

```plaintext
Input Image 
    ↓
YOLOv8 Detection 
    ↓
Crop Region of Interest (ROI) 
    ↓
EasyOCR Recognition 
    ↓
Output: Text + Confidence Score
