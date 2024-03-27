import ast  # Import the ast module

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
        try:
            decodedStr = decodedStr + item[0] * item[1]
        except:
            print(item)
    return decodedStr
def write_To_File(string_Value):
    with open('ASCII_Art_Compression.txt', 'w') as f:
        f.write(str(string_Value))
def extract_From_File():
    with open('ASCII_Art_Compression.txt', 'r') as g:
        fileContent = g.read()
        decode_List = ast.literal_eval(fileContent)
        return decode_List

tmp = """                   ******************
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



write_To_File(encodeTalker(tmp))  # First, write the encoded representation to a file
decodedList = extract_From_File()  # Extract the encoded list from the file
decodedString = decodeTalker(decodedList)  # Decode the list back into the original string
print(decodedString)  # Print the decoded ASCII art
