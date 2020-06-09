from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt

wykres=pd.read_csv("dane.csv")
ox=wykres['os.X'].values.tolist()
oy=wykres['os.Y'].values.tolist()
plt.xlabel("oś X")
plt.ylabel("oś Y")
plt.title("Przykładowy wykres")
plt.plot(ox, oy)
fig = plt.gcf()
plt.savefig('wykres.png')

root = Tk()
root.title("Proof of concept")
canvas = Canvas(root, width = 700, height = 500)
canvas.pack()
img = PhotoImage(file="wykres.png", master=root)
canvas.create_image(20,20, anchor=NW, image=img)
mainloop()