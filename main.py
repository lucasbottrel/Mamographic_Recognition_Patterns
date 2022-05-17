import time
from tkinter import *
from tkinter import filedialog
from imageio import imread
from skimage import *
from skimage import io
from PIL import Image, ImageTk

from haralick import *
from SVM import *

img_calc = None # image loaded for calculation
execution_time = 0 
filename = '' # image filename (path)
haralick_results = None
img_classification = None

# clear the image label on main screen
def clear_label_image():
    imgFrm.config(image='')

# upload file to main screen
def upload_file():
    clear_label_image()

    global img
    global img_calc
    global filename

    # accepted types for image files to upload
    f_types = (("Image files", "*.png *.jpeg"), ("All files", "*.*"))
    # read filename from update image screen
    filename = filedialog.askopenfilename(filetypes=f_types)

    # define image set to calculation
    img_calc = imread(filename)

    # define image to show on main screen
    img = (Image.open(filename))
    img = ImageTk.PhotoImage(img.resize((400, 400), Image.ANTIALIAS))
    imgFrm.config(image=img)
    imgFrm.pack()

def openSVM():
    SVMScreen = Tk()
    
    SVMScreen.wm_title("SVM Accuracy")
    SVMScreen.geometry('400x250')
    SVMScreen.config(background="white")

    # start execution time
    start = time.time()

    accuracy_score = run_SVM()
    
    # title of screen
    title = Label(SVMScreen, text="Accuracy", font=('', 24), anchor=CENTER, background='#5559fd', fg='white')
    title.place(x=30, y=20)
    
    # svm accuracy calculate and show
    accuracy = Label(SVMScreen, text=str(round(accuracy_score,2)) + '%', font=('', 24), anchor=CENTER, background='#fff', fg='black')
    accuracy.place(x=30, y=90)
    
    # end execution time
    execution_time = time.time() - start

    # Log Area
    bottomFrm = LabelFrame(SVMScreen, fg='#fff',text='Tempo de Execução', background='black')
    execTimeFrm = Label(bottomFrm, text=str(round(execution_time, 4)) + ' s', fg='white', background='black', font=('', 11))
    execTimeFrm.place(x=10, y=5)
    bottomFrm.place(relwidth=1, relheight=0.2, rely=0.8)

# Open haralick parameters screen
def openHaralick():
    
    global haralick_results
    
    # open screen
    haralickScreen = Tk()
    haralickScreen.wm_title("Haralick Calcs")
    haralickScreen.geometry('1120x400')
    haralickScreen.config(background="white")

    # title of screen
    title = Label(haralickScreen, text="Descritores de Haralick", font=('', 24), anchor=CENTER, background='#5559fd', fg='white')
    title.place(x=30, y=20)

    # start execution time
    start = time.time()

    # get haralick results from image
    haralick_results = haralick_calcs(img_calc)

    # C1 comatrix results
    c1 = Label(haralickScreen, text="C1 ", font=('', 14), background="white", fg='#5559fd')
    c1.place(x=30, y=80)

    # homogeneity
    homog_c1 = Label(haralickScreen, text="Homogeneidade: " + str(round(haralick_results[0].homogeneity, 3)), font=('', 12), background="white")
    homog_c1.place(x=30, y=120)

    # energy
    energ_c1 = Label(haralickScreen, text="Energia: " + str(round(haralick_results[0].energy, 3)), font=('', 12), background="white")
    energ_c1.place(x=30, y=160)

    # entropy
    entrop_c1 = Label(haralickScreen, text="Entropia: " + str( round(haralick_results[0].entropy, 3)), font=('', 12), background="white")
    entrop_c1.place(x=30, y=200)

    # C2 comatrix results
    c2 = Label(haralickScreen, text="C2 ", font=('', 14), background="white", fg='#5559fd')
    c2.place(x=250, y=80)

    # homogeneity
    homog_c2 = Label(haralickScreen, text="Homogeneidade: " + str(round(haralick_results[1].homogeneity, 3)), font=('', 12), background='white')
    homog_c2.place(x=250, y=120)

    # energy
    energ_c2 = Label(haralickScreen, text="Energia: " + str(round(haralick_results[1].energy, 3)), font=('', 12), background="white")
    energ_c2.place(x=250, y=160)
    
    # entropy
    entrop_c2 = Label(haralickScreen, text="Entropia: " + str(round(haralick_results[1].entropy, 3)), font=('', 12), background="white")
    entrop_c2.place(x=250, y=200)

    # C4 comatrix results
    c4 = Label(haralickScreen, text="C4 ", font=('', 14), background="white", fg='#5559fd')
    c4.place(x=470, y=80)

    # homogeneity
    homog_c4 = Label(haralickScreen, text="Homogeneidade: " + str(round(haralick_results[2].homogeneity, 3)), font=('', 12), background='white')
    homog_c4.place(x=470, y=120)

    # energy
    energ_c4 = Label(haralickScreen, text="Energia: " + str(round(haralick_results[2].energy, 3)), font=('', 12), background="white")
    energ_c4.place(x=470, y=160)

    # entropy
    entrop_c4 = Label(haralickScreen, text="Entropia: " + str(round(haralick_results[2].entropy, 3)), font=('', 12), background="white")
    entrop_c4.place(x=470, y=200)

    # C8 comatrix results
    c8 = Label(haralickScreen, text="C8 ", font=('', 14), background="white", fg='#5559fd')
    c8.place(x=690, y=80)

    # homogeneity
    homog_c8 = Label(haralickScreen, text="Homogeneidade: " + str(round(haralick_results[3].homogeneity, 3)), font=('', 12), background='white')
    homog_c8.place(x=690, y=120)

    # energy
    energ_c8 = Label(haralickScreen, text="Energia: " +str(round(haralick_results[3].energy, 3)), font=('', 12), background="white")
    energ_c8.place(x=690, y=160)

    # entropy
    entrop_c8 = Label(haralickScreen, text="Entropia: " + str(round(haralick_results[3].entropy, 3)), font=('', 12), background="white")
    entrop_c8.place(x=690, y=200)
    
    # C16 comatrix results
    c16 = Label(haralickScreen, text="C16 ", font=('', 14), background="white", fg='#5559fd')
    c16.place(x=910, y=80)

    # homogeneity
    homog_c16 = Label(haralickScreen, text="Homogeneidade: " + str(round(haralick_results[4].homogeneity, 3)), font=('', 12), background='white')
    homog_c16.place(x=910, y=120)

    # energy
    energ_c16 = Label(haralickScreen, text="Energia: " + str(round(haralick_results[4].energy, 3)), font=('', 12), background="white")
    energ_c16.place(x=910, y=160)
    
    # entropy
    entrop_c16 = Label(haralickScreen, text="Entropia: " + str(round(haralick_results[4].entropy, 3)), font=('', 12), background="white")
    entrop_c16.place(x=910, y=200)

    # end execution time
    execution_time = time.time() - start

    # Log Area
    bottomFrm = LabelFrame(haralickScreen, fg='#fff',text='Tempo de Execução', background='black')
    execTimeFrm = Label(bottomFrm, text=str(round(execution_time, 4)) + ' s', fg='white', background='black', font=('', 11))
    execTimeFrm.place(x=10, y=5)
    bottomFrm.place(relwidth=1, relheight=0.2, rely=0.8)

# resample the image by the number of shades passed
def resampling(shades):

    # recover the original image
    resampled_img = imread(filename)
    # find max value on the image to use by max on new image
    maxValue = resampled_img.max()

    # update all image pixels to the resample value 
    for i in range(len(resampled_img)):
        for j in range(len(resampled_img)):
            resampled_img[i][j] = resampled_img[i][j] / maxValue * shades

    # show resample image
    print(resampled_img)
    io.imshow(resampled_img, cmap='gray')
    io.show()

# image classification
def img_classify():
    global filename
    
    # recover image and calculate haralick descriptors
    img = imread(filename)
    results = haralick_calcs(img)
    
    global img_classification
    
    # update image classification
    img_classification = classify(results)
    
    # show classification of image on main screen
    classFrm = Label(bottomFrm, text=img_classification , fg='white', background='black', font=('', 16))
    classFrm.place(x=10, y=15)
    

# Main Screen
root = Tk()
root.wm_title("Mamographic Recognition Patterns")
root.geometry('1280x600')

# Menu Top
menubar = Menu(root)

# Image Menu
imgMenu = Menu(menubar, tearoff=0)
imgMenu.add_command(label="Nova Imagem", command=upload_file)
imgMenu.add_command(label="Substituir Imagem", command=upload_file)

# Calc Menu
calcMenu = Menu(menubar, tearoff=0)
calcMenu.add_command(label="Descritores de Haralick", command=openHaralick)

# Reamostragem Menu
reamosMenu = Menu(menubar, tearoff=0)
reamosMenu.add_command(label="32 tons de cinza",command=lambda: resampling(32))
reamosMenu.add_command(label="24 tons de cinza",command=lambda: resampling(24))
reamosMenu.add_command(label="16 tons de cinza", command=lambda: resampling(16))
reamosMenu.add_command(label="8 tons de cinza", command=lambda: resampling(8))
reamosMenu.add_command(label="4 tons de cinza", command=lambda: resampling(4))

# SVM Menu
svmMenu = Menu(menubar, tearoff=0)
svmMenu.add_command(label="Treinar / Testar", command=openSVM)
svmMenu.add_command(label="Classificar imagem", command=lambda: img_classify())
svmMenu.add_command(label="Matriz de Confusão", command=confusion_matrix)

# Main Menus
menubar.add_cascade(label="Imagem", menu=imgMenu)
menubar.add_cascade(label="Calcular", menu=calcMenu)
menubar.add_cascade(label="Reamostragem", menu=reamosMenu)
menubar.add_cascade(label="SVM", menu=svmMenu)

# display the menu
root.config(menu=menubar, background='white')

# Image Area
topFrm = Frame(root)
imgFrm = Label(topFrm, image='', background='white')
topFrm.place(relwidth=1, relheight=0.9, rely=0.05)
topFrm.configure(background='white')

# Classification Image Area
bottomFrm = LabelFrame(root, fg='#fff', text='Classificação da Imagem', background='black')
bottomFrm.place(relwidth=1, relheight=0.2, rely=0.8)

root.mainloop()
