import streamlit as st 
from  PIL import Image
import io,cv2,warnings,os
import numpy as np
from track_ import draw_rects, track_images, extract_text
from ultralytics import YOLO





model  =  YOLO("runs/detect/train/weights/best.pt")
st.sidebar.title("Number Plate Recognition")
warnings.filterwarnings("ignore")


sample_folder = "sample_images"
sample_list = ["None"] + os.listdir(sample_folder)
sample_choice = st.sidebar.selectbox("Choose Sample Image:", sample_list)


holder  = st.empty()

if sample_choice != "None":
    image_bytes = open(os.path.join(sample_folder, sample_choice), "rb")
else:
    image_bytes = holder.file_uploader("Choose a PNG file", type=["png","jpg"])




    
if image_bytes is not None:
    image =  np.array(Image.open(io.BytesIO(image_bytes.read())))
    
    holder.image(image, caption="Uploaded Image", use_container_width=True)
    
    if st.button("Detect IMAGE ->"):
        image_resized = cv2.resize(image,(640,640))
        
        holder.image(image_resized, caption="Resized Image", use_container_width=True)
        
        with st.spinner("Detecting..."):

            coordinates,conf,img =  track_images(image_resized,model)  
            full_rect_image =  draw_rects(image_resized,coordinates,color_text=(255,0,0),text_tuple="conf: {:.2f}%".format(conf))
            text,conf_text  =  extract_text(img)
            
            holder.empty()
            
            
            col1, col2  = st.columns(2)
            with col1:
                st.image(full_rect_image, caption="Detected Image", use_container_width=True)
            with col2:
                st.image(img[..., ::-1], caption="License plate ", use_container_width=True)
                
                
            st.markdown(f"**Detected Text:** {text} || **Confidence:** {conf_text*100:.2f}%")
            st.markdown(f"#### **confidence of detection**: {conf*100:.2f}%")