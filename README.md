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
>  Values on different lines
>  is like this zee.
>  '''

## Loops
### While Loops
- While loops are able to have an else statement:
  > while condition:
    > code
    > else
    >  other code
  
### For Loops
for value in 'Word':
print (value) --> This would print each value within "Word"
> for value in ['Woof' , 'Meow' , 'Human Noises']:
>
> print (value) --> This would print each value within the array

> for value in range (min , max, skip):
> 
> print(value) --> This would repeat the numbers from the min, to the max, skipping every skip value.

## Chars
- Find Character in string: 
> - Value = 'Hallo'
>  - Value[0] --> Start to end
> - Or
> - Value[-1] --> End to start
- print(value[0:3]) --> Displays all characters from 0 to 3
- let(value) --> Produces the total number of characters
- value.find("X") --> returns the first instance of the character within the string 
- value.replace("value 1","not a value") --> replaces the 'value 1' with not a value
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



## Practice Exercises
### Practice Exercise 1: Factorial Challenge
> Notes
> - Take input
> - if input is not num, return none (1.2,String variable Spam spam spam):
> - if input < 0, return none
> - if input = 0, return 1
> 
> total_Factorial = 1
> 
> user_Input = input("Please input value: ")
>  
> if user_Input.isdigit() and user_Input.isdecimal() and int(user_Input) > 0:
>     for current_Factorial in range(1, int(user_Input) + 1):
>         total_Factorial = current_Factorial * total_Factorial
>     print(total_Factorial)

> else:
>     print("None")

### Challenge 1: Terminal Scribe
> - from tkinter import *
> - root = Tk()
> - root.title('Zee - Terminal Scribe')
> - root.geometry("500x500")
> - tech_Container = Canvas(root, width=500, height=500, bg="white")
> - tech_Container.pack(pady=20)
> - square_Size = input("Input: ")
> - tech_Container.create_rectangle(0, 0, square_Size, square_Size, fill="blue")
> - root.mainloop()














# Python_Week-2

# Python_Week-3

# Python_Week-4


