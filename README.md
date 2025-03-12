![logo](https://github.com/Yashraghuvans/Vector-Visions/blob/main/logo.jpg)

# Vector-Visions

This repository contains a simple Python script to perform video segmentation using YOLOv8 and Ultralytics.

## Getting Started

### Prerequisites

* Python 3.7+
* pip

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/Yashraghuvans/Vector-Visions.git
    cd Vector-Visions
    ```

2.  Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3.  Download the YOLOv8 Nano model weights (`yolo11n.pt`) and place them in the root directory. You can download them from the ultralytics repository, or they are often downloaded automatically by the ultralytics library if they are missing.

4. Place your video file `video1.mp4` into the root directory.

### Usage

Run the `yolo.ipynb` script:

```bash
python yolo.ipynb
