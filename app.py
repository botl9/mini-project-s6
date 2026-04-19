"""Main application entry point"""

import os

os.environ['TF_USE_LEGACY_KERAS'] = '1'

import streamlit as st
from src.config import PAGE_TITLE, PAGE_ICON, LAYOUT, INITIAL_SIDEBAR_STATE

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state=INITIAL_SIDEBAR_STATE
)

st.markdown("""
<style>
    h1 { font-size: 2rem; font-weight: 600; color: #111; }
    h2 { font-size: 1.5rem; font-weight: 600; color: #111; }
    [data-testid="stMetric"] { background: #fafafa; padding: 1rem; border-radius: 8px; border: 1px solid #eee; }
    .stButton > button { background: #111; color: #fff; border: none; border-radius: 6px; }
    hr { margin: 1.5rem 0; border: none; border-top: 1px solid #eee; }
</style>
""", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

with col1:
    if st.button("Home", use_container_width=True):
        st.session_state.page = "home"
with col2:
    if st.button("Live Detection", use_container_width=True):
        st.session_state.page = "live"
with col3:
    if st.button("Motion Trigger", use_container_width=True):
        st.session_state.page = "motion"
with col4:
    if st.button("Analysis", use_container_width=True):
        st.session_state.page = "analysis"
with col5:
    if st.button("Model Info", use_container_width=True):
        st.session_state.page = "model"

st.markdown("---")

if "page" not in st.session_state:
    st.session_state.page = "home"

page = st.session_state.page

if page == "home":
    from src.pages.home import render_home
    render_home()
elif page == "live":
    from src.pages.live_detection import render_live_detection
    render_live_detection()
elif page == "motion":
    from src.pages.motion_trigger import render_motion_trigger
    render_motion_trigger()
elif page == "analysis":
    from src.pages.analysis import render_analysis
    render_analysis()
elif page == "model":
    from src.pages.model_info import render_model_info
    render_model_info()