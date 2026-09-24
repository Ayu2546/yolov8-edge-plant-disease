# Parse command-line arguments.
import argparse

from ultralytics import YOLO

parser = argparse.ArgumentParser()

# Specify a YOLO classification model to train (e.g., yolov8n-cls.pt).
parser.add_argument(
    "--model",
    type=str,
    required=True,
)

args = parser.parse_args()

# Load the specified YOLO classification model.
model = YOLO(args.model)

# Train the model.
model.train(
    data="data/strawberry",
    epochs=50,
    imgsz=224,
    batch=32,
    device=0,
    workers=8,
    seed=42,
    project="runs/classify",
    name=args.model.replace(".pt", ""),
)