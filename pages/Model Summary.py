import streamlit as st
import os 
from PIL import Image


st.markdown("""
            #   #Model Summary

## 🎯 Objective  
To accurately detect and extract vehicle number plates from images using a custom-trained YOLOv8 model combined with EasyOCR.

## 🏗️ Model Architecture

### 1. **YOLOv11 (Ultralytics)**
- Task: **Object Detection** — Locates the number plate in an image
- Output: Bounding box coordinates and confidence scores

### 2. **EasyOCR**
- Task: **Text Extraction (OCR)**
- Purpose: Reads the text inside the detected number plate region
- Output: Text and character-wise confidence score

## 🔬 Performance
- High detection precision using YOLOv8
- Fast and readable OCR output with average accuracy ~90%+
- Works well on various lighting and background conditions

## 🧪 Pipeline
```plaintext
[Input Image] 
     ⬇
[YOLOv8] → Detect number plate 
     ⬇
[Cropped ROI] → [EasyOCR] → Extract text 
     ⬇
[Final Output: Image with bounding box + Text + Confidence]

            
            
""")

image_paths = os.listdir("metrics")

num_cols = 2

# Display in columns
cols = st.columns(num_cols)

for idx, img_path in enumerate(image_paths):
    with cols[idx % num_cols]:
        st.image(Image.open(os.path.join("metrics",img_path)), use_container_width=True, caption=f"{img_path.split('.')[0]}")


