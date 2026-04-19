"""Home page"""

import streamlit as st

def render_home():
    st.title("CCTV Surveillance System")
    st.markdown("A computer vision system for real-time object detection in surveillance footage.")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Object Classes", "80+")
    col2.metric("Detection Speed", "Real-time")
    col3.metric("Model Size", "6 MB")
    col4.metric("Storage Saved", "70-90%")
    
    st.markdown("---")
    st.markdown("## Features")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Live Object Detection")
        st.write("Detect objects in CCTV footage using YOLO.")
    with col2:
        st.markdown("### Motion Triggered Recording")
        st.write("Only save footage when motion is detected.")
    
    st.markdown("---")
    st.markdown("## Quick Start")
    st.code("pip install -r Requirements.txt\nstreamlit run app.py", language="bash")