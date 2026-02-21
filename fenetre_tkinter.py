import tkinter as tk

racine = tk.Tk()
racine.title("Sudoku")
racine.geometry("1200x700")

canvas = tk.Canvas(racine, bg = "#000000", height=2800, width=2500)
canvas.place(anchor='center')

#
# Image
# https://stackoverflow.com/questions/3270209/how-do-i-make-tkinter-support-png-transparency
#
from PIL import ImageTk
photoimage = ImageTk.PhotoImage(file="Medias\SVB Plays.png")
canvas.create_image(1900, 1800, image=photoimage)

racine.mainloop()