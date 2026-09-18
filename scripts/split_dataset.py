# Handle file and directory paths.
from pathlib import Path

# Randomize the order of images.
import random

# Copy files.
import shutil


# Set a seed for reproducible randomization.
SEED = 42

TRAIN_RATIO = 0.70
VAL_RATIO = 0.15

DATA_DIR = Path("data")

SOURCE_DIRS = {
    "healthy": DATA_DIR / "strawberry_healthy",
    "diseased": DATA_DIR / "strawberry_diseased",
}

OUTPUT_DIR = DATA_DIR / "strawberry"


def split_dataset():
    random.seed(SEED)

    # Process each class separately.
    for class_name, source_dir in SOURCE_DIRS.items():
        images = list(source_dir.glob("*.JPG"))
        random.shuffle(images)

        total = len(images)
        train_end = int(total * TRAIN_RATIO)
        val_end = train_end + int(total * VAL_RATIO)

        splits = {
            # Up to train_end.
            "train": images[:train_end],

            # From train_end to val_end.
            "val": images[train_end:val_end],

            # From val_end to the end.
            "test": images[val_end:],
        }

        for split_name, split_images in splits.items():
            destination = OUTPUT_DIR / split_name / class_name
            destination.mkdir(parents=True, exist_ok=True)

            # Copy images here.
            for image in split_images:
                shutil.copy2(image, destination / image.name)

            print(
                f"{class_name:8} | "
                f"{split_name:5} | "
                f"{len(split_images):4} images"
            )


if __name__ == "__main__":
    split_dataset()