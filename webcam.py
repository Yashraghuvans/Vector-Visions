from ultralytics import YOLO
import time

# Load the YOLO model
model = YOLO("yolo11n.pt")

# Start time
start_time = time.time()

# Predict with the webcam as the source
results = model.predict(source=0, stream=True, save=True)

# Process results
for r in results:
    # Check if 30 seconds have passed
    if time.time() - start_time > 40:
        break

    # Access masks and boxes (if needed)
    masks = r.masks
    boxes = r.boxes

# Output path
output_path = "video.mp4"
print(f"Saved segmented video to {output_path}")
