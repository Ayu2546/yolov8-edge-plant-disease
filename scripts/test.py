from ultralytics import YOLO


def main():
    model = YOLO("runs/classify/yolov8n-cls/weights/best.pt")

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