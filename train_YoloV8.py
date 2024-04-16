from ultralytics import YOLO
import os

os.environ["CUDA_VISIBLE_DEVICES"] = '4,5,6,7' # List the GPUs

# Load a model
model = YOLO('yolov8m-seg.pt')  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data='/raid/abylay_turekhassim/v8/data.yaml', epochs=70, imgsz=600, device=[0,1,2,3], batch=16)