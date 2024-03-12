# Take input
# if input is not num, return none (1.2,String variable Spam spam spam)
# if input < 0, return none
# if input = 0, return 1
#my new changes
total_Factorial = 1
user_Input = input("Please input value: ")


if user_Input.isdigit() and user_Input.isdecimal() and int(user_Input) > 0:
    for current_Factorial in range(1, int(user_Input) + 1):
        total_Factorial = current_Factorial * total_Factorial
    print(total_Factorial)
else:
    print("None")


