"""Model loaders for CNN and YOLO models"""

import os
import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.optimizers import Adam

YOLO_MODEL = "yolov8n.pt"

@tf.keras.utils.register_keras_serializable()
def load_cnn_model():
    """Load pre-trained CNN model"""
    with open('model/model.json', 'r') as f:
        model_json = f.read()
    classifier = tf.keras.models.model_from_json(model_json)
    classifier.load_weights('model/model_weights.h5')
    classifier.compile(
        optimizer=Adam(learning_rate=0.001),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    return classifier

@tf.keras.utils.register_keras_serializable()
def load_yolo_model():
    """Load YOLO model"""
    from ultralytics import YOLO
    return YOLO(YOLO_MODEL)

def load_training_data():
    """Load CIFAR-10 training data"""
    with open('model/history.pckl', 'rb') as f:
        history = pickle.load(f)
    X_train = np.load('model/X.txt.npy')
    Y_train = np.load('model/Y.txt.npy')
    Y_train = Y_train.ravel()
    return history, X_train, Y_train

def get_cnn_accuracy(history):
    """Get CNN accuracy from training history"""
    return history['accuracy'][-1] * 100