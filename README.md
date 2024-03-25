# Python_Week-1
## Note: 
- Greyed out text refers to actual code
- (-->) Refers to comments

## General
- Print values: print(value)
- Strings can be multiplied: print("*" * 10)
- booleans must be upper case: True / False
- Scanner in Java: value = input(value) --> Always returns String value
- Conversion Types: int(value)
- type(value) returns type of value the input is.
- Specific to object = function
- else, method --> methods being value.upper(), function being print()

>  Value = ''' <br>
>  Values on different lines <br>
>  is like this zee. <br>
>  '''

## Loops
### While Loops
- While loops are able to have an else statement:
  > while condition:
    > code <br>
    > else <br>
    > other code 
  
### For Loops
> for value in 'Word': <br>
> print (value) --> This would print each value within "Word" <br>
> for value in ['Woof' , 'Meow' , 'Human Noises']: <br>
> print (value) --> This would print each value within the array <br>
> for value in range (min , max, skip): <br>
> print(value) --> This would repeat the numbers from the min, to the max, skipping every skip value.

## Chars
- Find Character in string: <br><br> 
> Value = 'Hallo'<br>
> Value[0] --> Start to end <br>
> Or <br>
> Value[-1] --> End to start <br>
- print(value[0:3]) --> Displays all characters from 0 to 3
- let(value) --> Produces the total number of characters
- value.find("X") --> returns the first instance of the character within the string  <br>
- value.replace("value 1","not a value") --> replaces the 'value 1' with not a value <br>
- print('Python' in value) --> this returns boolean if word is in string

## Formatted Strings
- Java: variable1 + "Random Text" + variable2
- Value = f'{variable1} Random Text {variable2}'

## Arithmetic
- value / value = decimal val
- value // value = integer
- value ** value = power
- round(x) --> method used to round numbers

## Logical Operators
- if bool_Val and not bool_Val2 --> means if val1 is true and val1 is false

## Alternative Number Types
Base 2 - Binary (0-1) <br> 
Base 8 - Octal (0-7) <br>
Base 10 - Decimal (0-9) <br> 
Base 16 - Hexadecimal (0-9, A-F) <br>

## Lists
> value_List = [1,2,3,4,5,6] <br>
> value_List = list(range(value))

--> adds 7 to list
> value_List.append(7) <br>

--> inserts 7 at the 3rd position <br>
> value_List.insert(7,2) <br>

--> removes item based on value, not index <br>
> value_List.remove(6) 

--> Removes last item in list <br>
> value_List.pop() 

--> copies list <br>
> value_List2 = value_List.copy 


## Tuples and Sets
Sets are random order

--> Removes all redundant data within the list
> myList = ['b', 'c', 'c'] <br>
> mySet = list(set(myList)) <br>
> print(myList) <br> 
> print(mySet) <br>

--> Adds element to set
> set.add()
--> Removes element to set
> set.discard()

Tuples are more efficient than lists because they take less memory, but cannot be modified. Useful for large amounts of data
--> Initialize a Tuple. (Access values using same logic as an array)
> myTuple = ('a','b','c')

## Dictionaries
--> Initialize Dictionary
> animamamals = {
>    'a': "apple", <br>
    'b': "bananana", <br>
    'c': "cawwot" <br>
}

--> Returns all keys within Dictionary
> animamamals.key()

--> Returns all values within Dictionary
> animamamals.values()

--> Takes key and returns values within Dictionary
> animamamals.get(value) 

## List Comprehensions
Its a one line way to make loops and if statements for a lists, instead of going the long way

--> 'item' can be changed to any variable name.
--> 2 * value multiplies the values by 2,
--> Order is: Arithmetic, loop, if statement
> my_List = list(range(value)) <br>
> filtered_List = [2*item for item in my_Lits if item % 10 == 0]

--> Split string into separate words based on specified character
> value = 'Hallo my good sir, how do you be doing?'
> print(value.split(values))

# Python_Week-2
## Functions
format: <br>
def functionName(parameters): <br>
  code <br>
  return --> if function needs to return a particular value <br>

### *args
*args would allow a user to input any variables within the parameters of a function <br>
> def function_Name(*args):
>   print(args)
> 
> function_Name(1,2,3)
> 
> output: (1,2,3)
Note when using this: <br>
"By adding the asterisk before args, Python understands that the variable name is just a reference to the arguments being passed in. This trick works only for positional arguments, not keyword arguments. If a keyword argument is passed in, an "unexpected keyword argument" error will occur."

### **kwargs (Keywords)
- Arguments are stored as a dictionary insead of tuple <br>
- Takes in the key plus the value of the element in a Dictionary <br>
> def function_Name(*args, **kwargs): <br>
> print(args) <br> 
> print(kwargs) <br>
>
> function_Name(1,2,3, operation='sum') <br>

> def function_Name(*args, operation='sum'): <br>
> if operation == 'sum': <br> 
>   return sum(args) <br>
> if operation == 'multiply': <br>
>  return math.prod(args) <br>

> function_Name(1,2,3,7,8, operation='sum') <br>
> Output: 27

### Text Processing in Python <br>
Various string modification methods within Python <br>
> text = "Insert Text Here" <br>
> punctuations = [',' , '.' , '*'] <br>
> text.loewr() <br> 
> text = text.replace(punctuation, '') <br>
 > text = text.replace('\n' , ' ') <br> 
> ' '.join([word for word in text.split() if len(word) > 3]) --> will remove short words

### Lambda
The expression is written as follows: variable = lambda parameters: expression <br>
> double = lambda x:x * 2 <br>
> multiply = lambda x, y: x * y <br> 
> add = lambda x, y, z: x + y + z <br>
> full_Name = lambda first_Name, last_Name: first_Name + " " + last_Name <br>
> age_Check = lambda age: True if age >= 18 else False <br>
> print(age_Check(18)) 

### Timed Variables
> print("Printed immediately.") <br>
> time.sleep(2.4)
> print("Printed after 2.4 seconds.")

### Classes
A static variable in a class is something that would not change at all at all.
Its a variable that is assigned within the class. <br>
Static Variables should be altered with Get and Set methods <br>

Creating a class is written as follows: <br>
> class wordSet: <br>
> def __init__(self): <br>
> self.words = set() <br>
>
> def addText(self,text): <br>
> text = Wordset.cleanText(text) <br>
> fot word in text.split(): <br>
> self.words.add(word) <br>
>
> def cleanText(text): <br>
> text = text.replace("!", '') --> replacing special characters with a space <br> 
> return text.lower() <br>
>
> wordSet = WordSet()
> wordSet.addText("Insert Text Here")
> wordSet.addText("Insert Other Text, Here!")

### Decorator
Written using the @ operator <br>
It allows the function to bypass using the self argument

> class wordSet: <br>
> replacePuncs = [Insert Special Characters Here]
> def __init__(self): <br>
> self.words = set() <br>
>
> def addText(self,text): <br>
> text = Wordset.cleanText(text) <br>
> fot word in text.split(): <br>
> self.words.add(word) <br>
>
> def cleanText(text): <br>
>  for punc in WordSet.replacePuncs <br>
>  text = text.replace(punc, '') --> replacing special characters with a space <br> 
> return text.lower() <br>
>
> wordSet = WordSet() <br>
> wordSet.addText("Insert Text Here") <br>
> wordSet.addText("Insert Other Text, Here!") <br>

### Class Inheritence
> class Class_Name: <br>
> code <br> 
>
> class Instanced_Class(Class_Name) <br>
>
### Try/Except 
> try: <br>
> code <br>
> except: Exception as e: <br>
> print(type(e)) <br>
>
Adding the "finally" keyword within the Try/Except logic would always run the code when the try and catch method is reached. <br> 
> try: <br>
> code <br>
> except: Exception as e: <br>
> print(type(e)) <br>
> finally: <br>
> print("This could will always run") <br>


# Python_Week-3
### Exception Handling (cont...)
Exceptions must be explicit <br>
Think of it like an if statement Zee <br>
List of Exceptions: <br>
- **AssertionError**      : Raised when an assert statement fails.
- **AttributeError**      :	Raised when attribute assignment or reference fails.
- **EOFError**            :	Raised when the input() function hits end-of-file condition.
- **FloatingPointError**  :	Raised when a floating point operation fails.
- **GeneratorExit**       :	Raise when a generator's close() method is called.
- **ImportError**         :	Raised when the imported module is not found.
- **IndexError**          :	Raised when the index of a sequence is out of range.
- **KeyError**            :	Raised when a key is not found in a dictionary.
- **KeyboardInterrupt**   :	Raised when the user hits the interrupt key (Ctrl+C or Delete).
- **MemoryError**         :	Raised when an operation runs out of memory.
- **NameError**           : Raised when a variable is not found in local or global scope.
- **NotImplementedError** :	Raised by abstract methods.
- **OSError**             :	Raised when system operation causes system related error.
- **OverflowError**       :	Raised when the result of an arithmetic operation is too large to be represented.
- **ReferenceError**      :	Raised when a weak reference proxy is used to access a garbage collected referent.
- **RuntimeError**        :	Raised when an error does not fall under any other category.
- **StopIteration**       :	Raised by next() function to indicate that there is no further item to be returned by iterator.
- **SyntaxError**         :	Raised by parser when syntax error is encountered.
- **IndentationError**    :	Raised when there is incorrect indentation.
- **TabError**            :	Raised when indentation consists of inconsistent tabs and spaces.
- **SystemError**         :	Raised when interpreter detects internal error.
- **SystemExit**          :	Raised by sys.exit() function.
- **TypeError**           :	Raised when a function or operation is applied to an object of incorrect type.
- **UnboundLocalError**   :	Raised when a reference is made to a local variable in a function or 
  method, but no value has been bound to that variable.
- **UnicodeError**        :	Raised when a Unicode-related encoding or decoding error occurs.
- **UnicodeEncodeError**  :	Raised when a Unicode-related error occurs during encoding.
- **UnicodeDecodeError**    :	Raised when a Unicode-related error occurs during decoding.
- **UnicodeTranslateError** :	Raised when a Unicode-related error occurs during translating.
- **ValueError**            :	Raised when a function gets an argument of correct type but improper value.
- **ZeroDivisionError**     :	Raised when the second operand of division or modulo operation is zero.


> try
> Exception Code
> except:
> other code --> can use keywords such as pass, which continues the code, continue, which would continue a loop, etc.

Best Practices for Exceptions:
> import logging <br>
> try: <br>
> code <br>
> except ValueError as e <br>
> code(e) <br>
> except ZeroDivisionError as e <br>
> pass <br>
> except Exception as e: <br>
> logging.exception(e) --> This could be for instance the time the program ran this




# Python_Week-4 


