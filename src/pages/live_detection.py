"""Live detection page"""

import streamlit as st
from src.models import load_yolo_model
from src.utils.video import process_video_with_yolo
from src.config import MAX_FRAMES

def render_live_detection():
    st.title("Live Object Detection")
    st.markdown("Upload a CCTV video to detect objects in real-time.")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        video_file = st.file_uploader("Select video file (MP4, AVI, MOV)", type=["mp4", "avi", "mov"])
        
        if video_file and st.button("RUN DETECTION"):
            with st.spinner("Processing video..."):
                input_path = "temp_input.mp4"
                with open(input_path, "wb") as f:
                    f.write(video_file.read())
                
                model = load_yolo_model()
                frames, detections, frame_count = process_video_with_yolo(input_path, model, MAX_FRAMES)
                
                if frames:
                    st.markdown("### Detection Results")
                    for i, (img, dets) in enumerate(zip(frames[::3], detections[::3])):
                        st.image(img, caption=f"Frame {i*3+1}: {', '.join(dets)}", use_container_width=True)
                    st.success(f"Processed {frame_count} frames")
    
    with col2:
        st.markdown("### Detectable Objects")
        st.info("80+ classes: Person, Car, Truck, Bus, Bicycle, Motorcycle, Dog, Cat, Bird, etc.")