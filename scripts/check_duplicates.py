import hashlib
from pathlib import Path


def calculate_sha256(file_path: Path) -> str:
    """Calculate the SHA-256 hash of a file."""

    sha256 = hashlib.sha256()

    # Read the file in chunks to avoid loading the entire file into memory.
    with file_path.open("rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)

    return sha256.hexdigest()


def collect_hashes(data_dir: Path) -> dict[str, list[Path]]:
    """Collect file paths grouped by their SHA-256 hashes."""

    hashes = {}

    for file_path in data_dir.rglob("*"):
        if file_path.is_file():
            hash_value = calculate_sha256(file_path)
            hashes.setdefault(hash_value, []).append(file_path)

    return hashes


def find_duplicates(hashes: dict[str, list[Path]]) -> dict[str, list[Path]]:
    """Find SHA-256 hashes associated with multiple files."""

    duplicates = {}

    for hash_value, file_paths in hashes.items():
        if len(file_paths) > 1:
            duplicates[hash_value] = file_paths

    return duplicates


def main():
    """Check the dataset for duplicate files using SHA-256 hashes."""
    
    data_dir = Path("data/strawberry")

    hashes = collect_hashes(data_dir)
    duplicates = find_duplicates(hashes)

    if duplicates:
        print("Duplicate files found:")

        for hash_value, file_paths in duplicates.items():
            print(f"\nSHA-256: {hash_value}")

            for file_path in file_paths:
                print(f"  {file_path}")
    else:
        print("No duplicate files found.")


if __name__ == "__main__":
    main()