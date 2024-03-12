from tkinter import *

root = Tk()
root.title('Zee - Terminal Scribe')
root.geometry("500x500")
tech_Container = Canvas(root, width=500, height=500, bg="white")
tech_Container.pack(pady=20)


square_Size = input("Input: ")
tech_Container.create_rectangle(0, 0, square_Size, square_Size, fill="blue")
root.mainloop()




