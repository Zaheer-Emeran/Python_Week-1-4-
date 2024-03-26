import numpy as np

# Take hex input
# Store each character in array
# Convert each letter to digit
# Multiply each digit to its respective power

# Add each digit to each other
# Add functionality so that two of the same letters needs to be converted as well

hex_Letters = ["A", "B", "C", "D", "E", "F"]
hex_Numbers = [10, 11, 12, 13, 14, 15]

user_Input = input("Please Enter A Hexadecimal Number To Be Converted Into Decimal: ").upper()
# separated_Input = [None] * user_Input.__sizeof__()

user_Input_Size = user_Input.__len__()
temp_Word_Array = [None] * user_Input_Size
final_Word_Array = [None] * user_Input_Size
test = [None] * user_Input_Size

for word_Temp in range(0, user_Input_Size):
    temp_Word_Array[word_Temp] = user_Input[word_Temp]  # Assigns character to array

for i in range(0, user_Input_Size):
    a = user_Input_Size - 1
    for z in range(0, hex_Letters.__len__()):
        if temp_Word_Array[i] == hex_Letters[z]:
            temp_Word_Array[i] = hex_Numbers[z]
        # print(f"Test {z}")
        # print(f"Hallo {i}")
    # print(int(temp_Word_Array[i]) + 1)
    user_Input_Size -= 1
    final_Word_Array[i] = pow(16, a)
    final_Word_Array[i] = float(final_Word_Array[i]) * float(temp_Word_Array[i])
final_Conversion = float(0)

print(sum(final_Word_Array))
