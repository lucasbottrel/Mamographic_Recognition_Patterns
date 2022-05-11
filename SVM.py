import os
from imageio import imread
from haralick import *
import csv

directory = None
#pega o diretório atual do programa
def getDirectory():
    global directory
    directory = os.getcwd()
    directory = str(directory)+"\Imagens"
    
getDirectory()

def getDescriptorsTraining():
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
            
        
getDescriptorsTraining()