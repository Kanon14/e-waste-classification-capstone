import sys, os
from ultralytics import YOLO
from ewasteDetection.pipeline.training_pipeline import TrainPipeline
from ewasteDetection.utils.main_utils import decodeImage, encodeImageIntoBase64, gen_frames
from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS, cross_origin
from ewasteDetection.constant.application import APP_HOST, APP_PORT


app = Flask(__name__)
CORS(app)

model = YOLO("../e-waste-classification-capstone/yolov11s_train/best.pt")
classNames = ['air-cond', 'audio-set', 'battery', 'fan', 'fridge', 
              'kettle', 'keyboard', 'laptop', 'light-source', 'microwave', 
              'mouse', 'pcb', 'printer', 'remote', 'smartphone', 
              'telephone', 'tv', 'usb', 'vape', 'washing-machine']


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        

@app.route("/train")
def trainRoute():
    obj = TrainPipeline()
    obj.run_pipeline()
    return "Training Successfully!!"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST", "GET"])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)
        
        os.system(f"cd yolov11s_train && yolo task=detect mode=predict \
                    model='best.pt' \
                    imgsz=640 \
                    source='../data/inputImage.jpg' \
                    conf=0.5")
        
        try:
            opencodedbase64 = encodeImageIntoBase64("yolov11s_train/runs/detect/predict/inputImage.jpg")
            result = {"image": opencodedbase64.decode('utf-8')}
        finally:
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
    return Response(gen_frames(model=model, classNames=classNames), mimetype='multipart/x-mixed-replace; boundary=frame')

  
if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host=APP_HOST, port=APP_PORT, debug=True)