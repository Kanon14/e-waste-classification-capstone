# 🤖 E-Waste-Classification-Capstone

## Project Overview
The E-Waste Detection Application is an innovative project leveraging AI-powered object detection to tackle the global e-waste problem. Using YOLO (You Only Look Once) models and a Streamlit-based interface, this application provides real-time e-waste detection via image uploads, webcams, and IP cameras. It aims to streamline e-waste classification, improving recycling efficiency and reducing environmental and health hazards.

## Features
1. E-Waste Problem Awareness
- Learn about the global e-waste crisis through detailed visualizations and informative content.
- Understand the environmental and health impacts of improper e-waste management.
2. Real-Time E-Waste Detection
- Image Detection: Upload an image and get instant e-waste classification results.
- Webcam Detection: Use your computer's webcam for live detection.
- IP Webcam Detection: Connect an IP camera for remote real-time detection.
3. AI Chatbot (Wall-E)
- Interact with Wall-E, an AI-powered chatbot for questions about e-waste.
- Powered by Llama3.2, it provides insightful responses to user queries.
4. Model Training
- Retrain the YOLO model using a simple interface.
- Export the model for further deployment on lightweight or edge devices.

## Project Setup
### Prerequisites
- Python 3.10+
- PyTorch 1.8+ [[Download PyTorch Cuda](https://pytorch.org/)]
- Compatible cuda toolkit and cudnn installed on your machine [[Nvidia GPU Capability](https://developer.nvidia.com/cuda-gpus)] [[Download Cuda Toolkit](https://developer.nvidia.com/cuda-toolkit)] (Note: You must have a [Nvidia Developer Account](https://developer.nvidia.com/login))
- Anaconda or Miniconda installed on your machine [[Download Anaconda](https://www.anaconda.com/download)]
- An ollama installed on your machine. [[Download Ollama](https://ollama.com/download)]
- Install LLM model compatible with your machine, information can be found in [Ollama](https://github.com/ollama/ollama)


### Installation
1. Clone the repository:
```bash
git clone https://github.com/Kanon14/e-waste-classification-capstone.git
cd e-waste-classification-capstone
```

2. Create and activate a Conda environment:
```bash
conda create -n ewaste python=3.10 -y
conda activate ewaste
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Training Data Source and Preparation
The training data is prepared in [capstone-kanon-2](https://universe.roboflow.com/computer-vision-learning-touhj/capstone-kanon-2) through the [Roboflow](https://roboflow.com/).

## Workflow
The project workflow is designed to facilitate a seamless transition from development to deployment:
1. `constants`: Manage all fixed variables and paths used across the project.
2. `entity`: Define the data structures for handling inputs and outputs within the system.
3. `components`: Include all modular parts of the project such as data preprocessing, model training, and inference modules.
4. `pipelines`: Organize the sequence of operations from data ingestion to the final predictions.
5. `application`: This is the main executable script that ties all other components together and runs the whole pipeline.

## How to Run
### Flask Application:
1. Execute the project:
```bash
python app.py
```
2. Then, access the application via your web browser:
```bash
open http://localhost:<port>
```
3. Execute the training pipeline:
```bash
http://localhost:<port>/train
```
4. To start real-time webcam detection:
```bash
http://localhost:<port>/video_feed
```
5. To start ip-webcam, specify the IPv4 address of your web camera
```bash
http://localhost:<port>/ip_video_feed
```
### Streamlit Application:
1. Execute the project: 
```bash
streamlit run streamlit_app.py
```
2. Then, access the application via your web browser:
```bash
open http://localhost:<port>
```