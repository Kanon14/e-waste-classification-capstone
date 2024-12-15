import streamlit as st
import cv2
import time
import numpy as np
import sys
from ultralytics import YOLO
from ewasteDetection.exception import AppException
from ewasteDetection.pipeline.training_pipeline import TrainPipeline

# Load the YOLO model
model = YOLO("../e-waste-classification-capstone/yolov11s_train/best.pt")

# Title
st.title("E-Waste Detection Application")

# Sidebar Menu
menu = st.sidebar.selectbox("Choose a feature", ["Train Model", "Image Detection", "Webcam Detection", "IP Webcam Detection"])

# Train Model
if menu == "Train Model":
    st.header("Train the E-Waste Detection Model")
    if st.button("Start Training"):
        st.info("Training in progress. Please wait...")
        obj = TrainPipeline()
        obj.run_pipeline()  # Trigger the training pipeline
        model.export(format="ncnn")  # Export the model for deployment
        st.success("Model training and export completed successfully!")

# Image Detection
elif menu == "Image Detection":
    st.header("Upload an Image for E-Waste Detection")
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        # Display uploaded image and results side by side
        col1, col2 = st.columns(2)

        # Read and decode the uploaded image
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)

        with col1:
            st.image(img, caption="Uploaded Image", use_container_width=True, channels="BGR")

        # Perform detection
        results = model(img)
        annotated_image = results[0].plot()

        with col2:
            st.image(annotated_image, caption="Detection Results", use_container_width=True, channels="BGR")

# Webcam Detection
elif menu == "Webcam Detection":
    st.header("Real-Time Detection from Webcam")
    
    # Create two columns for Start and Stop Buttons
    col1, col2 = st.columns(2)
    start_button = col1.button("Start Webcam")
    stop_button = col2.button("Stop Webcam")
    
    if start_button:
        video_placeholder = st.empty()  # Placeholder for displaying video frames
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # Open default webcam
        cap.set(3, 1280)  # Set frame width
        cap.set(4, 720)   # Set frame height
        cap.set(cv2.CAP_PROP_FOURCC, 0x32595559) # CAP_PROP_FOURCC: 4-character code of codec
        cap.set(cv2.CAP_PROP_FPS, 30)            # CAP_PROP_FPS: Frame rate
        
        try:
            while cap.isOpened():
                if stop_button: # Check if Stop button is pressed
                    st.info("Webcam stopped")
                    break
                ret, frame = cap.read()
                if not ret:
                    st.error("Failed to read from webcam")
                    break
            
                # Perform detection/tracking using YOLO model
                results =model.track(source=frame, verbose=False, device="cuda", stream=True, persist=True)
                for res in results:
                    annotated_frame = res.plot() # Annotate the frame with detection results
            
                # Display the frame with annotations
                video_placeholder.image(annotated_frame, use_container_width=True, channels="BGR")
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            raise AppException(e, sys)
        
        finally:
            cap.release() # Release webcam resource when done
            st.info("Webcam stopped")

# IP Webcam Detection
elif menu == "IP Webcam Detection":
    st.header("Real-Time Detection from IP Webcam")

    # Create two columns for Start and Stop Buttons
    col1, col2 = st.columns(2)
    start_button = col1.button("Start IP Webcam")
    stop_button = col2.button("Stop IP Webcam")

    ip_url = st.text_input("Enter IP Webcam URL (e.g., http://192.168.100.4:8080/video):")

    if start_button and ip_url:
        video_placeholder = st.empty()  # Placeholder for displaying video frames
        cap = cv2.VideoCapture(ip_url, cv2.CAP_FFMPEG)  # Open IP webcam feed
        cap.set(3, 640)  # Reduce resolution to 640x480 for performance
        cap.set(4, 480)
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 2)  # Increase buffer size
        cap.set(cv2.CAP_PROP_FPS, 10)  # Limit FPS

        try:
            while cap.isOpened():
                if stop_button:  # Check if Stop button is pressed
                    st.info("IP Webcam stopped")
                    break

                ret, frame = cap.read()
                if not ret:
                    st.warning("Failed to read from IP webcam. Skipping frame...")
                    continue  # Skip bad frames instead of breaking the loop

                # Perform detection using YOLO model
                try:
                    results = model.track(source=frame, verbose=False, device="cuda", stream=True, persist=True)
                    for res in results:
                        annotated_frame = res.plot()  # Annotate the frame with detection results

                    # Display the frame with annotations
                    video_placeholder.image(annotated_frame, use_container_width=True, channels="BGR")
                except Exception as e:
                    st.warning(f"Error during YOLO detection: {str(e)}. Skipping this frame...")

                # Optional: Add delay for stability
                time.sleep(0.05)  # Add a 50ms delay to reduce system load

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            raise AppException(e, sys)

        finally:
            cap.release()  # Release IP webcam resource when done
            st.info("IP Webcam stopped")

    elif start_button and not ip_url:
        st.error("Please enter a valid IP Webcam URL.")