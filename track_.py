from ultralytics import YOLO
import easyocr,warnings,cv2,os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


warnings.filterwarnings("ignore")



model  =  YOLO("runs/detect/train/weights/best.pt")


def draw_rects(image,coordinates=[],color_text=(0, 255, 0),color_box=(50, 50, 255),text_tuple=None):
    
    for rects in coordinates:
        x,y,w,h =  rects
        rect_image =cv2.rectangle(image,(x,y),(w,h),color_box, 2)
        if text_tuple :
            rect_image = cv2.putText(rect_image,text_tuple,(x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, color_text, 2)
    
    return rect_image




def track_images(image_, model):
    coordinates = []
    rect_images =  []
    # Run prediction and convert results to DataFrame
    results = model.predict(image_)[0].boxes.data.detach().cpu().numpy()
    df = pd.DataFrame(results,columns=["x1","y1","x2","y2","conf","class_id"]).astype("float")
    
    # Iterate through each detection
    for _, row in df.iterrows():
        x1, y1, x2, y2, conf,_ = row  # it has only one class thus not needed
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        coordinates.append([x1, y1, x2, y2])
        rect_image = image_[y1:y2, x1:x2]
        rect_images.append(rect_image)
    
    return (coordinates,conf,rect_images[0])



def extract_text(image):
    reader = easyocr.Reader(['en'], gpu=False)
    text_detections = reader.readtext(image)
    final_text = ""
    conf_text = 0.0
    for bbox, text, confidence in text_detections:
        final_text += text + " "
        conf_text += confidence
    
    conf_ =  conf_text/len(text_detections) if text_detections else 0.0
    return (final_text,conf_)
    


            
            
            
# image_path = cv2.imread("C:/Users/RISHABH/Pictures/images/plate2.jpg")
            
# """
# img : roi of full image conatins only number plate
# full_rect_image : full image with rectangle drawn on number plate
# text : extracted text from number plate
# conf : confidence of the extracted text

# """          
        
# coordinates,conf,img =  track_images(image_path,model)  
# full_rect_image =  draw_rects(image_path,coordinates,color_text=(255,50,50),text_tuple="conf: {:.2f}%".format(conf))[..., ::-1]
# text,conf_text  =  extract_text(img)



