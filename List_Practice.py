from datetime import datetime

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

tmp = """           *****************
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

print(encodeTalker(tmp))



for i in range(0 , length): # This would loop for as many line breaks there are
    line_Counter += 1
    line_Dictionary.update({line_Counter: tmp2[i]}) # Adds values to Dictionary

    length2 = line_Dictionary.get(line_Counter).split(' ')
    # print(length2)
    # print(length2)



    # print(decodeTalker(encodeTalker(length2)))

# length2 = line_Dictionary.get(2).split(' ')
for i in range(0,length2.__len__()):
    line_Counter2 += 1
    word_Dictionary.update({line_Counter2: length2[i]}) # Adds values to Dictionary




