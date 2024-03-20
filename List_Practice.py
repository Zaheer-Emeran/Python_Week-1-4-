#  /\_/\\
# ( o.o )
#  > ^ <
from datetime import datetime


# Take input
# Separate lil cat into one string
# identify which characters are used
# tally up each character
# display how many of each character is used
# encodeString() should take a value and convert it into Tuples. [('A' , 5) , ('B' , 3) , ('C' , 2) , ('D' , 10)]
# decodeString() should convert value from encode back to how it was


# user_Input = input("Please Insert Combination Of Characters (E.g. AABB2233222BBAA): ")

# user_Input = user_Input.split()

def encodeTalker(stringVal):
    encodedList = []
    prevChar = stringVal[0]
    count = 0
    for char in stringVal:
        if prevChar != char:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count = count + 1
    encodedList.append((prevChar, count))
    return encodedList

def decodeTalker(encodedList):
    decodedStr = ''
    for item in encodedList:
        decodedStr = decodedStr + item[0] * item[1]
    return decodedStr

tmp = """                    *****************
               ******               ******
           ****                           ****
        ****                                 ***
      ***                                       ***
     **           ***               ***           **
   **           *******           *******          ***
  **            *******           *******            **
 **             *******           *******             **
 **               ***               ***               **
**                                                     **
**       *                                     *       **
**      **                                     **      **
 **   ****                                     ****   **
 **      **                                   **      **
  **       ***                             ***       **
   ***       ****                       ****       ***
     **         ******             ******         **
      ***            ***************            ***
        ****                                 ****
           ****                           ****
               ******               ******
                    *****************"""

# print(encodeTalker(tmp))
# print(decodeTalker(encodeTalker(tmp)))



line_Counter = 0
line_Counter2 = 0
line_Counter3 = 0

line_Dictionary = {} # Initialized empty Dictionary
word_Dictionary = {} # Initialized empty Dictionary

length = len(tmp.split('\n')) # This would count how many lines are in the string

tmp2 = tmp.split('\n')

for i in range(0 , length): # This would loop for as many line breaks there are
    line_Counter += 1
    line_Dictionary.update({line_Counter: tmp2[i]}) # Adds values to Dictionary

    length2 = line_Dictionary.get(line_Counter).split(' ')
    print(length2)
    # print(length2)


    # print(decodeTalker(encodeTalker(length2)))

# length2 = line_Dictionary.get(2).split(' ')
for i in range(0,length2.__len__()):
    line_Counter2 += 1
    word_Dictionary.update({line_Counter2: length2[i]}) # Adds values to Dictionary




