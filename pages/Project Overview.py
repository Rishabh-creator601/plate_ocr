import streamlit as st 



st.sidebar.title("Project Overview")


st.markdown(""" 
# 🚀 Number Plate Recognition & OCR App

An end-to-end AI solution that detects and reads number plates from vehicle images.

## 🔍 What It Does
- 📸 Upload any vehicle image  
- 🎯 Detects the number plate using **YOLOv8**  
- 🔍 Extracts and reads the plate using **EasyOCR**  
- 🖥️ Streamlit-based web interface — responsive and user-friendly  

## ⚙️ Tech Stack
- `YOLOv11` (Ultralytics) for object detection  
- `EasyOCR` for text extraction  
- `OpenCV`, `NumPy`, `PIL` for image processing   

## 🧠 Use Cases
- Automated Parking Systems  
- Traffic Law Enforcement  

 

> ✅ Lightweight, fast, and runs locally with high accuracy  
 

         """)