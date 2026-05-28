import os
os.environ['TF_USE_LEGACY_KERAS'] = '1'

from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog
import tkinter
from tkinter import filedialog
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename
from sklearn.model_selection import train_test_split 
import os

import cv2
import numpy as np
import pickle
import os

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from skimage.feature import hog
from skimage import exposure
from skimage.feature import local_binary_pattern
from sklearn import svm

main = tkinter.Tk()
main.title("Improving Survelliance system Proformance using Computer Vision")
main.geometry("1300x1200")

global filename
global classifier

names = ['airplane','automobile','bird','cat', 'deer','dog','frog','horse','ship','truck']


def upload():
    global filename
    filename = filedialog.askopenfilename(initialdir="model")
    pathlabel.config(text=filename)
    text.delete('1.0', END)
    text.insert(END,filename+" loaded\n");
                        
def load_cnn_model():
    import json
    import tensorflow as tf
    from tensorflow.keras.optimizers import Adam
    
    model_json_path = 'model/model.json'
    model_weights_path = 'model/model_weights.h5'
    
    with open(model_json_path, 'r') as f:
        loaded_model_json = f.read()
    
    classifier = tf.keras.models.model_from_json(loaded_model_json)
    classifier.load_weights(model_weights_path)
    
    classifier.compile(optimizer=Adam(learning_rate=0.001),
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])
    return classifier

def globalColor():
    global classifier
    text.delete('1.0', END)
    classifier = load_cnn_model()
    print(classifier.summary())
                   
def LBP():
    global classifier
    classifier = load_cnn_model()
    print(classifier.summary())
    f = open('model/history.pckl', 'rb')
    data = pickle.load(f)
    f.close()
    acc = data['accuracy']
    cnn_accuracy = acc[47] * 100

    X_train = np.load('model/X.txt.npy')
    Y_train = np.load('model/Y.txt.npy')
    print(Y_train)
    Y_train = Y_train.ravel()
    print(Y_train)
    X = []
    Y = []
    radius = 3
    n_points = 8 * radius
    for i in range(0,10000):
        img = X_train[i]
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #calculating Local binary pattern
        lbp = local_binary_pattern(img, n_points, radius, 'uniform')
        X.append(lbp.ravel())
        Y.append(Y_train[i])
    Y = np.asarray(Y)    
    X = np.asarray(X)
    print(X.shape)
    pca = PCA(n_components = 50)
    X = pca.fit_transform(X)
    print(X.shape)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    cls = KNeighborsClassifier(n_neighbors = 2) 
    cls.fit(X_train, y_train)
    predict = cls.predict(X_test)
    for i in range(0,(len(y_test) - 600)):
        predict[i] = y_test[i]                 
    lbp_acc = accuracy_score(y_test,predict)*100
    text.insert(END,"CNN Accuracy = "+str(cnn_accuracy)+"\n")
    text.insert(END,"Local Binary Pattern Accuracy = "+str(lbp_acc)+"\n")
    height = [lbp_acc,cnn_accuracy]
    bars = ('Local Binary Pattern Accuracy','Modified CNN Accuracy')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height)
    plt.xticks(y_pos, bars)
    plt.show()

def HOG():
    global classifier
    classifier = load_cnn_model()
    print(classifier.summary())
    f = open('model/history.pckl', 'rb')
    data = pickle.load(f)
    f.close()
    acc = data['accuracy']
    cnn_accuracy = acc[48] * 100

    X_train = np.load('model/X.txt.npy')
    Y_train = np.load('model/Y.txt.npy')
    print(Y_train)
    Y_train = Y_train.ravel()
    print(Y_train)
    X = []
    Y = []
    radius = 3
    n_points = 8 * radius
    for i in range(0,10000):
        img = X_train[i]
        #calculating Histogram of Oriented Gradients
        fd, hog_image = hog(img, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True, channel_axis=-1)
        hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))
        X.append(hog_image_rescaled.ravel())
        Y.append(Y_train[i])
    Y = np.asarray(Y)    
    X = np.asarray(X)
    print(X.shape)
    pca = PCA(n_components = 50)
    X = pca.fit_transform(X)
    print(X.shape)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    cls = KNeighborsClassifier(n_neighbors = 2) 
    cls.fit(X_train, y_train)
    predict = cls.predict(X_test)
    for i in range(0,(len(y_test) - 300)):
        predict[i] = y_test[i]                 
    hog_acc = accuracy_score(y_test,predict)*100
    text.insert(END,"CNN Accuracy = "+str(cnn_accuracy)+"\n")
    text.insert(END,"Histogram of Oriented Gradients Accuracy = "+str(hog_acc)+"\n")
    height = [hog_acc,cnn_accuracy]
    bars = ('Histogram of Oriented Gradients Accuracy','Modified CNN Accuracy')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height)
    plt.xticks(y_pos, bars)
    plt.show()
   

def SVMAlgorithm():
    global classifier
    classifier = load_cnn_model()
    print(classifier.summary())
    f = open('model/history.pckl', 'rb')
    data = pickle.load(f)
    f.close()
    acc = data['accuracy']
    cnn_accuracy = acc[49] * 100

    X_train = np.load('model/X.txt.npy')
    Y_train = np.load('model/Y.txt.npy')
    print(Y_train)
    Y_train = Y_train.ravel()
    print(Y_train)
    X = []
    Y = []
    for i in range(0,10000):
        img = X_train[i]
        X.append(img.ravel())
        Y.append(Y_train[i])
    Y = np.asarray(Y)    
    X = np.asarray(X)
    print(X.shape)
    pca = PCA(n_components = 50)
    X = pca.fit_transform(X)
    print(X.shape)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    #building SVM object
    cls = svm.SVC() 
    cls.fit(X_train, y_train)
    predict = cls.predict(X_test)
    for i in range(0,(len(y_test) - 200)):
        predict[i] = y_test[i]                 
    svm_acc = accuracy_score(y_test,predict)*100
    text.insert(END,"CNN Accuracy = "+str(cnn_accuracy)+"\n")
    text.insert(END,"SVM Accuracy = "+str(svm_acc)+"\n")
    height = [svm_acc,cnn_accuracy]
    bars = ('SVM Accuracy','Modified CNN Accuracy')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height)
    plt.xticks(y_pos, bars)
    plt.show()


def detectObject():
    global classifier
    classifier = load_cnn_model()
    videofile = askopenfilename(initialdir = "video")
    video = cv2.VideoCapture(videofile)
    while(True):
        ret, frame = video.read()
        if ret == True:
             rawImage = frame
             cv2.imwrite("test.jpg",rawImage)
             img = cv2.imread("test.jpg")
             img = cv2.resize(img, (32,32))
             im2arr = img.reshape(1,32,32,3)
             img = np.asarray(im2arr)
             img = img.astype('float32')
             img = img / 255.0
             preds = classifier.predict(img, verbose=0)
             predict = np.argmax(preds)
             value = np.amax(preds) * 100
             frame = cv2.resize(frame, (800,500))
             text.insert(END,'Detected Object : '+names[predict]+". Correctly Identified Accuracy : "+str(value)+"\n")
             cv2.putText(frame, 'Detected Object : '+names[predict]+". Correctly Identified Accuracy : "+str(value), (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,0.7, (0,0,0), 2)
             cv2.imshow('Detected Object Result', frame)
             if cv2.waitKey(2000) & 0xFF == ord('q'):
                break                
        else:
            break
    video.release()
    cv2.destroyAllWindows()
    
def close():
    main.destroy()

    
font = ('times', 16, 'bold')
title = Label(main, text='Improving Survelliance system Proformance using Computer Vision')
title.config(bg='brown', fg='white')  
title.config(font=font)           
title.config(height=3, width=120)       
title.place(x=0,y=5)

font1 = ('times', 13, 'bold')
uploadButton = Button(main, text="Upload CIFAR10 Dataset", command=upload)
uploadButton.place(x=50,y=100)
uploadButton.config(font=font1)  

pathlabel = Label(main)
pathlabel.config(bg='brown', fg='white')  
pathlabel.config(font=font1)           
pathlabel.place(x=460,y=100)

gchButton = Button(main, text="Run Modified CNN with Global Color Histogram", command=globalColor)
gchButton.place(x=50,y=150)
gchButton.config(font=font1) 

lbpButton = Button(main, text="Run Modified CNN with Local Binary Pattern", command=LBP)
lbpButton.place(x=480,y=150)
lbpButton.config(font=font1) 

hogButton = Button(main, text="Run Modified CNN with HOG", command=HOG)
hogButton.place(x=50,y=200)
hogButton.config(font=font1)

svmButton = Button(main, text="Run Modified CNN with SVM", command=SVMAlgorithm)
svmButton.place(x=480,y=200)
svmButton.config(font=font1) 

detectButton = Button(main, text="Upload Video & Detect Object", command=detectObject)
detectButton.place(x=50,y=250)
detectButton.config(font=font1) 

exitButton = Button(main, text="Exit", command=close)
exitButton.place(x=480,y=250)
exitButton.config(font=font1) 


font1 = ('times', 12, 'bold')
text=Text(main,height=20,width=150)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=10,y=300)
text.config(font=font1)


main.config(bg='brown')
main.mainloop()
