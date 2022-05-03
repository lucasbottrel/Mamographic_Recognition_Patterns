from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
import funcoesMenu as menu

# MAIN FRAME
root = Tk()
root.wm_title("Mamographic Recognition Patterns")
root.geometry('1280x720')

# TOP BAR
menu.menuFunc(root)

# ÁREA DA IMAGEM
topFrm = LabelFrame(root, text="imagem")
topFrm.place(relwidth=1, relheight=0.75)
topFrm.configure(background='white')

# ÁREA DE LOG
bottomFrm = LabelFrame(root, text="terminal", fg='#fff')
bottomFrm.place(relwidth=1, relheight=0.25, rely=0.75)
bottomFrm.configure(background='black')

root.mainloop()
