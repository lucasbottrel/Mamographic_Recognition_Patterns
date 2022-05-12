from genericpath import exists
import os
from imageio import imread
from haralick import *
import csv
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
from skimage import io
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import plot_confusion_matrix
from matplotlib import pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

directory = None
classifier = None
Y_Test = None
X_Test = None

#pega o diretório atual do programa
def getDirectory():
    global directory
    directory = os.getcwd()
    directory = str(directory)+"\Imagens"
    

def getFileDescriptorsTraining():
    global directory
    arqDataSet = open("dataBase.csv", "w+", newline='', encoding='utf-8')
    writeFile = csv.writer(arqDataSet)
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

def run_SVM():

    global classifier
    global Y_Test
    global X_Test
    
    getDirectory()

    existsFile = str(os.getcwd()) + "\dataBase.csv"

    #create(if not exists) and load dataset
    if not (os.path.exists(existsFile)):
        getFileDescriptorsTraining()
        descriptors_data = read_csv(existsFile)
    else:#load dataset
        descriptors_data = read_csv(existsFile)

    #Split the data in training and testing subsets
    splitDatabase = descriptors_data.values

    X = splitDatabase[:,0:15]
    Y = splitDatabase[:,15]

    X_Training, X_Test, Y_Training, Y_Test = train_test_split(X,Y,test_size=0.25)

    #Classifier training using Suport Vector Machine(SVM)
    classifier = SVC(kernel='linear')
    # training SVM
    classifier.fit(X_Training, Y_Training)
    #Check classifier accuracy on test data and see result
    predict_MP = classifier.predict(X_Test)
    accuracy = accuracy_score(Y_Test, predict_MP) * 100
    
    return accuracy

def confused_matrix():
    # Generate confusion matrix
    matrix = plot_confusion_matrix(classifier, X_Test, Y_Test,
                                    cmap=plt.cm.Blues,
                                    normalize=None,
                                    )
    plt.title('Matriz de Confusão')
    plt.show()
    
def compare_matrix():
    
    predict_MP = classifier.predict(X_Test)
    y_result = np.concatenate((predict_MP.reshape(len(predict_MP),1), Y_Test.reshape(len(Y_Test),1)),1)
    
    print(y_result)

def classify(results):
    test = [[round(results[0].homogeneity,3),round(results[1].homogeneity,3),round(results[2].homogeneity,3),round(results[3].homogeneity,3),round(results[4].homogeneity,3),
                                round(results[0].energy,3),round(results[1].energy,3),round(results[2].energy,3),round(results[3].energy,3),round(results[4].energy,3),
                                round(results[0].entropy,3),round(results[1].entropy,3),round(results[2].entropy,3),round(results[3].entropy,3),round(results[4].entropy,3)]]
    
    
    
    if(classifier.predict(test)[0] == 1):
        return 'BIRADS1'
    elif(classifier.predict(test)[0] == 2):
        return 'BIRADS2'
    elif(classifier.predict(test)[0] == 3):
        return 'BIRADS3'
    elif(classifier.predict(test)[0] == 4):
        return 'BIRADS4'