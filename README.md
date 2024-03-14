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




# Python_Week-2

# Python_Week-3

# Python_Week-4


