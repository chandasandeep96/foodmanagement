import tkinter
from tkinter import PhotoImage
root=tkinter.Tk()#creates an window
root.title("Food Donation Form")
root.geometry("800x1000")
image_path=PhotoImage(file=r"D:\698\project\github files\backgroundimage.png")
bg_image=tkinter.Label(root,image=image_path)
bg_image.place(relheight=1,relwidth=1)
root.mainloop()
