from genericpath import exists
import os
from imageio import imread
from haralick import *
import csv
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 
from sklearn.svm import SVC


directory = None
#pega o diretório atual do programa
def getDirectory():
    global directory
    directory = os.getcwd()
    directory = str(directory)+"\Imagens"
    
getDirectory()

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
model = SVC()
model.fit(X_Training, Y_Training)
#Check classifier accuracy on test data and see result
predict_MP = model.predict(X_Test)
print("Accuracy: ", accuracy_score(Y_Test, predict_MP))