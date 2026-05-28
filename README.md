# Improving Surveillance System Performance Using Computer Vision

![Python](https://img.shields.io/badge/python-3.9+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-lightgrey)
![GitHub repo size](https://img.shields.io/github/repo-size/botl9/mini-project-s6)

A semester 6 mini project that implements object detection in video surveillance using CNN (Convolutional Neural Network) combined with various computer vision techniques.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [GUI Features](#gui-features)
- [Model Architecture](#model-architecture)
- [Technical Details](#technical-details)
- [Known Issues & Solutions](#known-issues--solutions)
- [Output](#output)
- [References](#references)
- [License](#license)

## Project Overview

This project demonstrates an enhanced surveillance system that uses deep learning and traditional computer vision methods for object detection and classification. The system compares the performance of CNN alone versus hybrid approaches combining CNN with:

- **Global Color Histogram (GCH)** - Color-based feature extraction
- **Local Binary Pattern (LBP)** - Texture-based feature extraction  
- **Histogram of Oriented Gradients (HOG)** - Edge-based feature extraction
- **Support Vector Machine (SVM)** - Classical ML classifier

## Dataset

The model is trained on the **CIFAR-10** dataset, which contains 60,000 32x32 color images in 10 classes:
- airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck

## Project Structure

```
SOURCE CODE/
├── GUI.py                      # Main application with Tkinter GUI
├── Requirements.txt            # Python dependencies
├── model/
│   ├── model.json              # Model architecture
│   ├── model_weights.h5        # Trained model weights
│   ├── history.pckl            # Training history
│   ├── X.txt.npy              # Training images (10,000 samples)
│   └── Y.txt.npy              # Training labels
├── video/
│   └── video.avi              # Sample video for testing
├── testImages/                 # Test images (1-8.jpg)
├── test.jpg                   # Temporary test image
└── IJIRT154669_PAPER.pdf      # Research paper reference
```

## Installation

### Prerequisites
- Python 3.9+
- TensorFlow
- OpenCV
- NumPy
- Scikit-learn
- Scikit-image
- Matplotlib
- Tkinter (usually comes with Python)

### Install Dependencies

```bash
pip install tensorflow keras opencv-python numpy scikit-learn scikit-image matplotlib pillow
```

Or use the Requirements.txt:
```bash
pip install -r Requirements.txt
```

## Running the Application

```bash
python GUI.py
```

## GUI Features

| Button | Function |
|--------|----------|
| **Upload CIFAR10 Dataset** | Load the dataset for processing |
| **Run Modified CNN with Global Color Histogram** | Compare CNN with GCH feature extraction |
| **Run Modified CNN with Local Binary Pattern** | Compare CNN with LBP feature extraction |
| **Run Modified CNN with HOG** | Compare CNN with HOG feature extraction |
| **Run Modified CNN with SVM** | Compare CNN with SVM classifier |
| **Upload Video & Detect Object** | Upload a video and detect objects in real-time |
| **Exit** | Close the application |

## Model Architecture

```
Layer 1: Conv2D (64 filters, 3x3) → MaxPooling2D
Layer 2: Conv2D (32 filters, 3x3) → MaxPooling2D
Layer 3: Flatten
Layer 4: Dense (256 units, ReLU)
Layer 5: Dense (10 units, Softmax)
```

**Total Parameters:** ~318,000

## Technical Details

### Feature Extraction Methods

1. **Global Color Histogram**: Computes RGB color histograms (256 bins per channel) and applies PCA for dimensionality reduction.

2. **Local Binary Pattern (LBP)**: Extracts texture patterns using uniform LBP with radius=3 and 24 points.

3. **HOG**: Uses 8 orientations, 16x16 pixel cells, and 1x1 cell blocks for edge detection.

4. **SVM**: Applies PCA (50 components) to raw pixels and classifies using Support Vector Machine.

### Comparison Metrics

The application displays bar charts comparing:
- Modified CNN Accuracy (from training history)
- Feature extraction method accuracy (using KNN or SVM classifiers)

## Known Issues & Solutions

| Issue | Solution |
|-------|----------|
| Model loading fails | Set `TF_USE_LEGACY_KERAS=1` environment variable |
| Deprecated Keras imports | Updated to use `tensorflow.keras` |
| Missing dependencies | Run `pip install -r Requirements.txt` |

## Output

- Accuracy comparison bar charts
- Real-time object detection on video
- Detected object labels and confidence scores

## References

- CIFAR-10 Dataset: https://www.cs.toronto.edu/~kriz/cifar.html
- Paper: IJIRT154669_PAPER.pdf

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.