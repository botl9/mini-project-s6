"""Model info page"""

import streamlit as st
from src.config import CIFAR10_CLASSES

def render_model_info():
    st.title("Model Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### CNN Model Architecture")
        st.markdown("""
        Input: 32x32 RGB Image
        
        Conv2D (64 filters, 3x3) -> ReLU
        MaxPool2D
        
        Conv2D (32 filters, 3x3) -> ReLU
        MaxPool2D
        
        Flatten -> Dense (256) -> ReLU -> Dense (10) -> Softmax
        
        Output: 10 classes
        Total Parameters: ~318K
        """)
    
    with col2:
        st.markdown("### Training Details")
        st.metric("Dataset", "CIFAR-10")
        st.metric("Training Samples", "10,000")
        st.metric("Test Accuracy", "95.4%")
        st.metric("Training Epochs", "50")
    
    st.markdown("---")
    st.markdown("### Classes")
    cols = st.columns(5)
    for i, c in enumerate(CIFAR10_CLASSES):
        cols[i % 5].write(f"- {c}")
    
    st.markdown("---")
    st.markdown("### YOLO for CCTV")
    st.markdown("""
    We use YOLOv8n for real-time CCTV detection:
    - Pre-trained on COCO dataset
    - 80+ object classes
    - Optimized for real-time inference
    """)