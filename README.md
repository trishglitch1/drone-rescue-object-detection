# Drone-Based Object Detection for Rescue Operations

A vision-based object detection system designed for UAVs (drones) in search 
and rescue operations, built using YOLOv8 and OpenCV.

Developed during the **India Space Week Internship**

## Project Overview

In rescue operations, drones can cover large areas quickly but require 
real-time analysis of aerial footage. This project implements an automated 
object detection pipeline that identifies humans, vehicles, bicycles, 
and other objects from drone footage — helping rescuers locate survivors faster.

## Detected Classes

| Object | Use in Rescue |
|---|---|
| Person | Locate survivors |
| Vehicle | Identify accessible routes |
| Bicycle | Detect human presence |
| Chair | Identify occupied areas |


## Tech Stack

- **Python**
- **YOLOv8** (Ultralytics) - Pre-trained object detection model
- **OpenCV** - Video processing and frame analysis
- **Math** - Python library for mathematical operations.


## Project Structure
drone-rescue-object-detection/
│
├── scripts/
│   ├── project.py        # Main detection script
│   └── fps.py            # FPS performance measurement
│
├── data/                 # Input video footage
├── results/              # Output screenshots with detections
├── docs/
│   ├── report of project.pdf
│   └── India Space Week training certificate.pdf
│
└── requirements.txt

## Installation & Usage

1. Clone the repository:
https://github.com/trishglitch1/drone-rescue-object-detection.git
2. Install dependencies:
pip install -r requirements.txt
3. Run the detection script:
python scripts/project.py

## Results

- Detected **4+ object classes** in real-time video footage
- **Confidence Scores:** 60–95% across all detected classes
- **Performance:** 10–15 FPS on standard hardware
- Achieved smooth inference using YOLOv8n (nano) pre-trained weights
- Processed video at real-time speeds measured via FPS counter

> Sample detection outputs are available in the `/results` folder


## Documentation

- 📝 [Project Report](docs/report%20of%20project.pdf)
- 🏅 [Internship Certificate](docs/India%20Space%20Week%20training%20certificate.pdf)


## Future Improvements

- Train a custom YOLOv8 model on aerial/drone-specific datasets
- Add GPS tagging to detected objects
- Integrate with live drone feed for real-time deployment
- Build a dashboard for rescue team monitoring

## Author

**Trisha**  
[GitHub](https://github.com/trishglitch1)
