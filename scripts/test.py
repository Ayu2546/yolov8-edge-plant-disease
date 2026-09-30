import argparse
from pathlib import Path
from ultralytics import YOLO

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--model",
        type=str,
        required=True,
    )

    args = parser.parse_args()
    
    model_name = Path(args.model).stem

    model = YOLO(
        f"runs/classify/{model_name}/weights/best.pt"
    )

    metrics = model.val(
        data="data/strawberry",
        split="test",
        imgsz=224,
        batch=32,
        device=0,
        workers=8,
        plots=True,
        name="yolov8n-cls-test",
    )

    print(f"Top-1 Accuracy: {metrics.top1}")
    print(f"Top-5 Accuracy: {metrics.top5}")


if __name__ == "__main__":
    main()