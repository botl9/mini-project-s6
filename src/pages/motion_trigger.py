"""Motion trigger page"""

import streamlit as st
from src.utils.video import detect_motion
from src.config import MAX_FRAMES

def render_motion_trigger():
    st.title("Motion Triggered Recording")
    
    st.markdown("""
    Traditional CCTV records 24/7. This system saves only when motion is detected, saving 70-90% storage.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Comparison")
        st.markdown("""
        | Approach | Storage/Day | Useful % |
        |---------|-----------|---------|
        | 24/7 Recording | 100 GB | 5% |
        | Motion Trigger | 10-30 GB | 80% |
        """)
    with col2:
        st.markdown("### How It Works")
        st.markdown("""
        1. Compare consecutive frames
        2. Calculate pixel differences
        3. If changes > threshold, save
        """)
    
    st.markdown("---")
    st.markdown("### Try Motion Detection")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        video_file = st.file_uploader("Test with your video", type=["mp4", "avi", "mov"])
        
        if video_file and st.button("ANALYZE MOTION"):
            with st.spinner("Analyzing motion..."):
                input_path = "motion_input.mp4"
                with open(input_path, "wb") as f:
                    f.write(video_file.read())
                
                frames, motion_count, total_count = detect_motion(input_path, MAX_FRAMES)
                
                for img in frames:
                    st.image(img, use_container_width=True)
                
                saved = motion_count * 100 // total_count if total_count > 0 else 0
                st.success(f"Motion: {motion_count}/{total_count} frames would be saved ({saved}%)")
    
    with col2:
        st.markdown("### Legend")
        st.markdown("- Green box: Moving object")
        st.markdown("- Red text: No motion")