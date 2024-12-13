import streamlit as st
import cv2
import time
import numpy as np
from ultralytics import YOLO
# from ewasteDetection.utils.main_utils import decodeImage, encodeImageIntoBase64, gen_frames

# Load the YOLO model
model = YOLO("../e-waste-classification-capstone/yolov11s_train/best.pt")
classNames = ['air-cond', 'audio-set', 'battery', 'fan', 'fridge', 
              'kettle', 'keyboard', 'laptop', 'light-source', 'microwave', 
              'mouse', 'pcb', 'printer', 'remote', 'smartphone', 
              'telephone', 'tv', 'usb', 'vape', 'washing-machine']

# Title
st.title("E-Waste Detection Application")

# Sidebar Menu
menu = st.sidebar.selectbox("Choose a feature", ["Image Detection", "Webcam Detection", "IP Webcam Detection"])

# Image Detection
if menu == "Image Detection":
    st.header("Upload an Image for E-Waste Detection")
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        # Display uploaded image
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        st.image(img, caption="Uploaded Image", use_container_width=True, channels="BGR")

        # Perform detection
        results = model(img)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cls = int(box.cls[0])
                conf = round(float(box.conf[0]) * 100, 2)
                currentClass = classNames[cls]
                # Draw bounding box and label on the image
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(img, f'{currentClass} {conf}%', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        st.image(img, caption="Detection Results", use_container_width=True, channels="BGR")

# Webcam Detection
elif menu == "Webcam Detection":
    st.header("Real-Time Detection from Webcam")
    if st.button("Start Webcam"):
        cap = cv2.VideoCapture(0)
        cap.set(3, 1280)  # Width
        cap.set(4, 720)   # Height

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Perform detection
            results = model(frame, stream=True)
            for r in results:
                boxes = r.boxes
                for box in boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cls = int(box.cls[0])
                    conf = round(float(box.conf[0]) * 100, 2)
                    currentClass = classNames[cls]
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f'{currentClass} {conf}%', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Display real-time detection
            st.image(frame, channels="BGR")

        cap.release()

# IP Webcam Detection
elif menu == "IP Webcam Detection":
    st.header("Real-Time Detection from IP Webcam")
    ip_url = st.text_input("Enter IP Webcam URL (e.g., http://192.168.100.4:8080/video):")

    if st.button("Start IP Webcam Detection"):
        if ip_url:
            cap = cv2.VideoCapture(ip_url)
            cap.set(3, 1280)  # Width
            cap.set(4, 720)   # Height

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                # Perform detection
                results = model(frame, stream=True)
                for r in results:
                    boxes = r.boxes
                    for box in boxes:
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        cls = int(box.cls[0])
                        conf = round(float(box.conf[0]) * 100, 2)
                        currentClass = classNames[cls]
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.putText(frame, f'{currentClass} {conf}%', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # Display real-time detection
                st.image(frame, channels="BGR")

            cap.release()
        else:
            st.error("Please enter a valid IP webcam URL.")
