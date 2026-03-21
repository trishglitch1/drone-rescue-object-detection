#Object detection model for rescue operations
#Trisha samal
#YOLOv8n.pt

import cv2
import numpy as np
import math
from ultralytics import YOLO
import time

def process_drone_feed(source):
    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture(source)

    prev_time = time.time()
    fps = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cur_time = time.time()
        time_delta = cur_time - prev_time
        if time_delta > 0:
            fps = 1.0 / time_delta
        prev_time = cur_time

        frame = cv2.resize(frame, (640, 640))
        h, w = frame.shape[:2]
        results = model(frame, verbose=False)[0]
        boxes = results.boxes.xyxy.cpu().numpy() if len(results.boxes) > 0 else []
        confs = results.boxes.conf.cpu().numpy() if len(results.boxes) > 0 else []
        clses = results.boxes.cls.cpu().numpy() if len(results.boxes) > 0 else []

        for box, conf, cls in zip(boxes, confs, clses):
            if conf < 0.6:
                continue
            x1, y1, x2, y2 = map(int, box)
            center_x = math.floor((x1 + x2) / 2)
            color = (0, 0, 255) if w*0.4 <= center_x <= w*0.6 else (0, 255, 0)
            distance = int(1000 / (y2 - y1 + 1))
            label = f"{model.model.names[int(cls)]} {conf:.2f} D:{distance}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1-8), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
        cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
        cv2.imshow("Drone HUD", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_drone_feed("street.mp4")

#Confidence score helps to make the detections reliable and reduces the chances of false detections
#IOU helps to avoid creating two bounding boxes for the same object, by keeping the more accurate one