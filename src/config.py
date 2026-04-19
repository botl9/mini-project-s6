import os

os.environ['TF_USE_LEGACY_KERAS'] = '1'

PAGE_TITLE = "CCTV Surveillance System"
PAGE_ICON = "CCTV"
LAYOUT = "wide"
INITIAL_SIDEBAR_STATE = "expanded"

MODEL_DIR = "model"
YOLO_MODEL = "yolov8n.pt"
MAX_FRAMES = 50

CIFAR10_CLASSES = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

MOTION_THRESHOLD = 500
GAUSSIAN_BLUR = 21
DIFF_THRESHOLD = 25