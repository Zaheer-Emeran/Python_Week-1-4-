import numpy as np

# Take hex input
# Store each character in array
# Convert each letter to digit

# Multiply each digit to its respective power
# Add each digit to each other
# Add functionality so that two of the same letters needs to be converted as well

hex_Letters = ["A", "B", "C", "D", "E", "F"]
hex_Numbers = [10, 11, 12, 13, 14, 15]
print(hex_Letters[0])




user_Input = input("Please Enter A Hexadecimal Number To Be Converted Into Decimal: ").upper()
# separated_Input = [None] * user_Input.__sizeof__()

user_Input_Size = user_Input.__len__()
temp_Word_Array = [None] * user_Input_Size
final_Word_Array = [None] * user_Input_Size
test = [None] * user_Input_Size

for word_Temp in range(0, user_Input_Size):
    temp_Word_Array[word_Temp] = user_Input[word_Temp]  # Assigns character to array

for i in range(0 , user_Input_Size):
    for z in range(0,hex_Letters.__len__()):
        if temp_Word_Array[i] == hex_Letters[z]:
            temp_Word_Array[i] = hex_Numbers[z]
        #print(f"Test {z}")
        #print(f"Hallo {i}")
    #print(int(temp_Word_Array[i]) + 1)


print(temp_Word_Array)

    #for total_Words in range(0,hex_Letters.__len__() - 1):

        #if temp_Word_Array[word_Temp] == hex_Letters[total_Words]: #
          #  print('')
            # print('Hallo')
            # print(hex_Numbers[total_Words])


