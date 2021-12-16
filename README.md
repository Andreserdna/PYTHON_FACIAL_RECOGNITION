# PYTHON_FACIAL_RECOGNITION
a facial recognition program using opencv. please make sure you have opencv2 installed and numpy
Please Follow the folder structure
- assets
- dataset
- YML
- video_logs_text

To use this program you must execute the following scripts in order for it to function properly

- face_data_capture.py -> This executes the face data capture and stores the data under dataset
- face_trainer_multiple.py -> This grabs all the images under the "dataset" folder and trains the model. Creates a YML file under "YML" folder
- initate_house_camera.py -> Initiates the camera and does the real time detection. Stores all of the data under "video_logs_text"