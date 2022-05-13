import os
from imageio import imread
import csv
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, plot_confusion_matrix, confusion_matrix
from matplotlib import pyplot as plt
import numpy as np

from haralick import *

directory = None # actual directory
classifier = None # classifier instance
Y_Test = None # Class test
X_Test = None # Descriptors test

# get actual directoy
def getDirectory():
    global directory
    directory = os.getcwd()
    directory = str(directory)+"\Imagens"
    
# get all image files to train
def getFileDescriptorsTraining():
    global directory
    
    # open dataset file to train SVM
    arqDataSet = open("dataBase.csv", "w+", newline='', encoding='utf-8')
    writeFile = csv.writer(arqDataSet)
    
    # fill dataset with haralick descriptors for each image
    i = 0
    for folder, subFolder, fileNames in os.walk(directory):
        for newFile in fileNames:
            completeWay = os.path.join(folder, newFile)
            im = imread(completeWay)
            dataB = haralick_calcs(im)
            writeFile.writerow([round(dataB[0].homogeneity,3),round(dataB[1].homogeneity,3),round(dataB[2].homogeneity,3),round(dataB[3].homogeneity,3),round(dataB[4].homogeneity,3),
                                round(dataB[0].energy,3),round(dataB[1].energy,3),round(dataB[2].energy,3),round(dataB[3].energy,3),round(dataB[4].energy,3),
                                round(dataB[0].entropy,3),round(dataB[1].entropy,3),round(dataB[2].entropy,3),round(dataB[3].entropy,3),round(dataB[4].entropy,3),i])
        
        i= i+1
            
    arqDataSet.close()

# run SVM instance
def run_SVM():

    global classifier
    global Y_Test
    global X_Test
    
    # recover actual directory
    getDirectory()

    # verify if the file already exists
    existsFile = str(os.getcwd()) + "\dataBase.csv"

    # create dataset (if not exists) and load dataset
    if not (os.path.exists(existsFile)):
        getFileDescriptorsTraining()
        descriptors_data = read_csv(existsFile)
    else:#load dataset
        descriptors_data = read_csv(existsFile)

    # Split the data in training and testing subsets
    splitDatabase = descriptors_data.values

    X = splitDatabase[:,0:15]
    Y = splitDatabase[:,15]

    X_Training, X_Test, Y_Training, Y_Test = train_test_split(X,Y,test_size=0.25)

    # Classifier training using Suport Vector Machine(SVM)
    classifier = SVC(kernel='linear')
    # Training SVM
    classifier.fit(X_Training, Y_Training)
    # Check classifier accuracy on test data and see result
    predict_MP = classifier.predict(X_Test)

    cm = confusion_matrix(Y_Test, predict_MP)

    print('Confusion Matrix : \n', cm)
    
    total1=sum(sum(cm))
    # from confusion matrix calculate accuracy
    accuracy=(cm[0,0]+cm[1,1]+cm[2,2]+cm[3,3])/total1 * 100

    sensitivity = cm[0,0]/(cm[0,0]+cm[1,1]+cm[2,2]+cm[3,3]) * 100

    specificity = cm[1,1]/(cm[0,0]+cm[1,1]+cm[2,2]+cm[3,3]) * 100
    
    return [accuracy, sensitivity, specificity]

# create and show confusion matrix
def show_confusion_matrix():
    # Generate confusion matrix
    matrix = plot_confusion_matrix(classifier, X_Test, Y_Test,
                                    cmap=plt.cm.Blues,
                                    normalize=None,
                                    )
    plt.title('Matriz de Confusão')
    plt.show()

# classify image
def classify(results):
    test = [[round(results[0].homogeneity,3),round(results[1].homogeneity,3),round(results[2].homogeneity,3),round(results[3].homogeneity,3),round(results[4].homogeneity,3),
                                round(results[0].energy,3),round(results[1].energy,3),round(results[2].energy,3),round(results[3].energy,3),round(results[4].energy,3),
                                round(results[0].entropy,3),round(results[1].entropy,3),round(results[2].entropy,3),round(results[3].entropy,3),round(results[4].entropy,3)]]
    
    # return the class of image
    if(classifier.predict(test)[0] == 1):
        return 'BI-RADS I'
    elif(classifier.predict(test)[0] == 2):
        return 'BI-RADS II'
    elif(classifier.predict(test)[0] == 3):
        return 'BI-RADS III'
    elif(classifier.predict(test)[0] == 4):
        return 'BI-RADS IV'