# Parse command-line arguments.
import argparse

parser = argparse.ArgumentParser()

# Specify a YOLO classification model to train (e.g., yolov8n-cls.pt).
parser.add_argument(
    "--model",
    type=str,
    required=True,
)

args = parser.parse_args()

print(args.model)