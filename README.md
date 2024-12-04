# e-waste-classification-capstone

## Project Overview
This capstone project addresses the inefficiencies and health risks associated with manual e-waste sorting by developing an automated system leveraging deep learning and computer vision. The project employs the YOLO (You Only Look Once) object detection algorithm to classify e-waste components with high accuracy, aiming to streamline e-waste management processes and reduce human exposure to hazardous materials.

## Project Setup
### Prerequisites
- Python 3.10+
- PyTorch 1.8+
- Compatible cuda toolkit and cudnn installed on your machine [[Nvidia GPU Capability](https://developer.nvidia.com/cuda-gpus)] [[Download Cuda Toolkit](https://developer.nvidia.com/cuda-toolkit)] (Note: You must have a [Nvidia Developer Account](https://developer.nvidia.com/login))
- Anaconda or Miniconda installed on your machine [[Anaconda Download](https://www.anaconda.com/download)].

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
The training data is prepared in [capstone-kanon-2](https://universe.roboflow.com/computer-vision-learning-touhj/capstone-kanon-2) through the Roboflow.

## Workflow
The project workflow is designed to facilitate a seamless transition from development to deployment:
1. `constants`: Manage all fixed variables and paths used across the project.
2. `entity`: Define the data structures for handling inputs and outputs within the system.
3. `components`: Include all modular parts of the project such as data preprocessing, model training, and inference modules.
4. `pipelines`: Organize the sequence of operations from data ingestion to the final predictions.
5. `app.py`: This is the main executable script that ties all other components together and runs the whole pipeline.

## How to Run
### Training and Image Detection:
1. Execute the project:
```bash
python app.py
```
2. Then, access the application via your web browser:
```bash
open http://localhost:<port>
```