# yolov8-edge-plant-disease

This project evaluates the effects of YOLOv8 model size and quantization on plant disease classification performance on edge devices.

## Training Environment

The YOLOv8 training environment was tested with the following configuration:

* OS: Windows 11
* Python: 3.12.7
* Ultralytics: 8.4.155
* PyTorch: 2.14.0+cu130
* Torchvision: 0.29.0+cu130
* CUDA: 13.0
* GPU: NVIDIA GeForce RTX 4090 (24 GB)

### Setup

Create a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell prevents the activation script from running, temporarily allow it for the current PowerShell session:

```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
.\.venv\Scripts\Activate.ps1
```

Install CUDA-enabled PyTorch:

```powershell
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu130
```

Install the project dependencies:

```powershell
pip install -r requirements.txt
```

Verify the environment:

```powershell
yolo checks
```

The GPU should be detected as `NVIDIA GeForce RTX 4090`.