# Accident Detection System

## 1. Demonstration
Watch this demonstration video:
[![Demonstration Video](https://img.youtube.com/vi/elPecFUnPg4/0.jpg)](https://www.youtube.com/watch?v=elPecFUnPg4)

## 2. What is Accident Detection System?
An Accident Detection System is designed to detect accidents via video or CCTV footage. Road accidents are a significant problem worldwide, causing many casualties. This repository primarily explores how CCTV can detect these accidents with the assistance of Deep Learning.

## 3. Prerequisites
To use this project, it's recommended to have Python Version > 3.8.

Clone this repository:

[https://github.com/franckessi237/Mod-le_D-tection_d_Accidents_Voiture.git](https://github.com/franckessi237/Mod-le_D-tection_d_Accidents_Voiture.git)

## 4. Getting Started - How to use it?

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/franckessi237/Mod-le_D-tection_d_Accidents_Voiture.git
    cd Mod-le_D-tection_d_Accidents_Voiture
    ```
2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Execution
Before running the program, you need to run the `training_object_detection_on_custom_dataset.ipynb`. Results are saved to the `runs/detect/train3` file. Then, to run this Python program, execute the `main.py` Python file.
/content/gdrive/MyDrive/Projet_IA/model.zip 
Follow these steps:

1. **Create the model:** Run the `training_object_detection_on_custom_dataset.ipynb` on Google Colab and check the Drive folder link containing the training dataset.

2. **Run the main program:** After creating the model, execute the `main.py` file to start the main program.
    ```bash
    python main.py
    ```

## 5. Description

### Project Structure
- `main.py`: Main script for accident detection.
- `image.py`: Script to extract images from the video.
- `best.pt`: Pre-trained YOLO model.

### Model and Training
The YOLO model is used to detect objects in the video. The detected objects are then analyzed to identify accidents.

### Real-Time Integration
The `main.py` script processes video frames in real-time and displays detection results with bounding boxes around the detected objects.

## Contributions
Contributions are welcome. Please open an issue to discuss significant changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
