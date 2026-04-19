"""Video processing utilities"""

import cv2
import numpy as np
from src.config import MAX_FRAMES, MOTION_THRESHOLD, GAUSSIAN_BLUR, DIFF_THRESHOLD


def process_video_with_yolo(video_path, model, max_frames=MAX_FRAMES):
    """Process video frames with YOLO detection"""
    cap = cv2.VideoCapture(video_path)
    frames, detections, frame_count = [], [], 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        result = model(frame, verbose=False)[0]
        annotated = result.plot(line_width=2)
        rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
        frames.append(rgb)
        
        frame_dets = []
        for i in range(len(result.boxes)):
            cls_id = int(result.boxes.cls[i].item())
            conf = float(result.boxes.conf[i].item()) * 100
            frame_dets.append(f"{result.names[cls_id]} ({conf:.0f}%)")
        detections.append(frame_dets if frame_dets else ["No detection"])
        
        if frame_count >= max_frames:
            break
    cap.release()
    return frames, detections, frame_count


def detect_motion(video_path, max_frames=MAX_FRAMES):
    """Detect motion using frame differencing"""
    cap = cv2.VideoCapture(video_path)
    ret, prev_frame = cap.read()
    if not ret:
        return [], 0, 0
    
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    prev_gray = cv2.GaussianBlur(prev_gray, (GAUSSIAN_BLUR, GAUSSIAN_BLUR), 0)
    
    frames, motion_count, total_count = [], 0, 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        total_count += 1
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (GAUSSIAN_BLUR, GAUSSIAN_BLUR), 0)
        
        diff = cv2.absdiff(prev_gray, gray)
        thresh = cv2.threshold(diff, DIFF_THRESHOLD, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        has_motion = False
        for c in contours:
            if cv2.contourArea(c) > MOTION_THRESHOLD:
                has_motion = True
                motion_count += 1
                cv2.rectangle(frame, cv2.boundingRect(c), (0, 255, 0), 2)
        
        if not has_motion:
            cv2.putText(frame, "NO MOTION", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        if total_count % 5 == 0:
            frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        prev_gray = gray
        
        if total_count >= max_frames:
            break
    cap.release()
    return frames, motion_count, total_count