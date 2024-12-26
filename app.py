import sys, os
from ultralytics import YOLO
from ewasteDetection.pipeline.training_pipeline import TrainPipeline
from ewasteDetection.utils.main_utils import decodeImage, encodeImageIntoBase64, gen_frames
from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS, cross_origin
from ewasteDetection.constant.application import APP_HOST, APP_PORT

# Initialize the Flask application
app = Flask(__name__)
CORS(app) # Enable Cross-Origin Resource Sharing for the application

# Class names for object detection
classNames = ['air-cond', 'audio-set', 'battery', 'fan', 'fridge', 
              'kettle', 'keyboard', 'laptop', 'light-source', 'microwave', 
              'mouse', 'pcb', 'printer', 'remote', 'smartphone', 
              'telephone', 'tv', 'usb', 'vape', 'washing-machine']


# ClientApp class to manage input files
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        

@app.route("/train")
def trainRoute():
    """
    Endpoint to train the YOLO model.
    - Runs the training pipeline.
    - Quantizes and saves the trained model for real-time deployment.
    """
    obj = TrainPipeline()
    obj.run_pipeline()
    model = YOLO("../e-waste-classification-capstone/yolov11s_train/best.pt") # Load the trained model
    model.export(format="ncnn") # Quantize and save the model for real-time implementation
    return "Training Successfully!!"


@app.route("/")
def home():
    """
    Endpoint to render the homepage.
    """
    return render_template("index.html")


@app.route("/predict", methods=["POST", "GET"])
@cross_origin()
def predictRoute():
    """
    Endpoint for prediction.
    - Accepts a base64-encoded image.
    - Runs the prediction using the trained YOLO model.
    - Returns the annotated image as a base64-encoded string.
    """
    try:
        image = request.json['image'] # Extract image from the request
        decodeImage(image, clApp.filename) # Decode and save the image
        
        # Run the YOLO prediction on the saved image
        os.system(f"cd yolov11s_train && yolo task=detect mode=predict \
                    model='best.pt' \
                    device='cuda' \
                    imgsz=640 \
                    source='../data/inputImage.jpg' \
                    conf=0.5")
        
        try:
            # Encode the output image to base64 and return it
            opencodedbase64 = encodeImageIntoBase64("yolov11s_train/runs/detect/predict/inputImage.jpg")
            result = {"image": opencodedbase64.decode('utf-8')}
        finally:
            # Cleanup prediction outputs
            os.system("rm -rf yolov11s_train/runs")
        
    except ValueError as val:
        print(val)
        return Response("Value not found inside json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        print(f"Error occurred: {e}")
        return Response("Something went wrong")
    
    return jsonify(result)


@app.route('/video_feed')
def video_feed():
    """
    Endpoint for real-time video feed from a webcam.
    - Streams annotated video frames with detections.
    """
    model = YOLO("../e-waste-classification-capstone/yolov11s_train/best.pt") # Instantiate the model
    model.to("cuda") # Connect the model to the CUDA GPU
    return Response(gen_frames(model=model, classNames=classNames, videoSource=0), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/ip_video_feed')
def ip_video_feed():
    """
    Endpoint for real-time video feed from an IP webcam.
    - Streams annotated video frames with detections from the specified IP webcam.
    """
    IP_WEBCAM_URL = "http://192.168.100.4:8080/video"  # Replace with your IP webcam URL
    model = YOLO("../e-waste-classification-capstone/yolov11s_train/best.pt") # Instantiate the model
    model.to("cuda") # Connect the model to the CUDA GPU
    
    # Modify gen_frames to accept a video source (default: 0 for webcam)
    return Response(gen_frames(model=model, classNames=classNames, videoSource=IP_WEBCAM_URL), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    

if __name__ == "__main__":
    # Initialize the client app and run the Flask application
    clApp = ClientApp()
    app.run(host=APP_HOST, port=APP_PORT, debug=True)