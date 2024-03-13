from tkinter import *
import numpy as np

# this is random code
root = Tk()
root.title('Zee - Terminal Scribe')
root.geometry("500x500")
tech_Container = Canvas(root, width=500, height=500, bg="white")
tech_Container.pack(pady=20)


# For the fun of it
# Choose amount of squares (max 3)
# Make the user choose between ten colours for each square
# Max Val = 500
# Min Val = ?

def colour_Selector(Input):
    print("hello")


colour_Of_Squares = [None] * 5

print("Select The Amount of Squares (1,2,3)")
total_Squares = (input("Square Input: "))

if total_Squares.isdigit() and int(total_Squares) <= 3:
    square_Size = (input("Input Size For Main Square: "))
    var = int(square_Size)
    for i in range(0, int(total_Squares)):
        colour_Input_Temp = input(f"Colour Input For Square {i + 1}. (R) Red, (G) Green, (B) Blue: ")
        if colour_Input_Temp == "R":
            colour_Of_Squares[i] = "Red"

        elif colour_Input_Temp == "G":
            colour_Of_Squares[i] = "Green"

        elif colour_Input_Temp == "B":
            colour_Of_Squares[i] = "Blue"

        tech_Container.create_rectangle(10, 10, var, var, fill = colour_Of_Squares[i])
        var = var / 2

    root.mainloop()

else:
    print("Invalid Value!")

