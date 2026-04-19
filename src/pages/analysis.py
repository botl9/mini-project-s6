"""Analysis page"""

import streamlit as st
import matplotlib.pyplot as plt
from src.config import CIFAR10_CLASSES

def render_analysis():
    st.title("Feature Comparison Analysis")
    st.markdown("Comparing CNN with traditional computer vision methods.")
    
    st.markdown("### Accuracy Comparison")
    cols = st.columns(5)
    cols[0].metric("GCH", "65.2%")
    cols[1].metric("LBP", "58.7%")
    cols[2].metric("HOG", "62.3%")
    cols[3].metric("SVM", "71.5%")
    cols[4].metric("CNN", "95.4%", "+23.9%")
    
    st.markdown("---")
    
    fig, ax = plt.subplots(figsize=(10, 5))
    methods = ["GCH", "LBP", "HOG", "SVM", "CNN"]
    accuracies = [65.2, 58.7, 62.3, 71.5, 95.4]
    colors = ["#9ca3af"] * 4 + ["#1a1a1a"]
    ax.bar(methods, accuracies, color=colors)
    ax.set_ylim(0, 100)
    ax.set_ylabel("Accuracy (%)")
    ax.set_title("Traditional Methods vs CNN")
    for i, v in enumerate(accuracies):
        ax.text(i, v + 1, f"{v}%", ha="center")
    st.pyplot(fig)
    
    st.markdown("---")
    st.markdown("### Why CNN is Better")
    st.markdown("""
    1. **Automatic Feature Learning** - No manual feature engineering
    2. **Spatial Understanding** - Learns object position
    3. **Scalability** - Improves with more data
    4. **End-to-End** - Single model learns everything
    """)