# Create x and y access in one colour
# Add numbers to each point
# Take input from user (x and y input)
# Draw a line from the center to the users x and y input

from tkinter import *
import numpy as np

# this is random code
root = Tk()
root.title('Zee - Terminal Scribe')
root.geometry("500x500")
tech_Container = Canvas(root, width=360, height=360, bg="white")
tech_Container.pack(pady=20)

# For the fun of it
# Choose amount of squares (max 3)
# Make the user choose between ten colours for each square
# Max Val = 500
# Min Val = ?

x_Axis = int(input("Please Enter X Coordinate Value. Max is 160 (x,y): "))

y_Axis = int(input(f"Please Enter Y Coordinate Value: Max is 160 ({x_Axis},y): "))

# if x is positive, choose between 180 and 345
# if y is positive, choose between 15 and 180
# if x is negative, choose between 15 and 180
# if y is negative, choose between 180 and 345


if x_Axis <= 160 and y_Axis <= 180:
    x_Axis = 180 + x_Axis
    y_Axis = 180 - y_Axis

tech_Container.create_line(180, 180, x_Axis, y_Axis, fill="red")

tech_Container.create_line(30, 180, 330, 180, fill="blue")
tech_Container.create_line(180, 30, 180, 330, fill="green")
tech_Container.create_text(180, 15, text="90", fill="green")
tech_Container.create_text(15, 180, text="360", fill="blue")
tech_Container.create_text(345, 180, text="270", fill="blue")
tech_Container.create_text(180, 345, text="180", fill="green")
root.mainloop()
