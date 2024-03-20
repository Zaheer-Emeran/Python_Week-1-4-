# QUIT = "quit"
# user_Input = input("User Input: ").lower()
#
# if user_Input.isdigit():
#     for i in range(0 , int(user_Input)):
#         print(f"This Code Would Run Till "
#               f"({i + 1}) is {int(user_Input)}")
# else:
#     print("Input is not a digit")
#
#














# Take Input /
# Loop through for length of input /
# Must be greater than 1 /
# Must be divisible by itself to get 1
# Must be divisible by 1

natrual_Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
user_Input = input("Please input a value: ")
#
for i in range(1 , natrual_Numbers.__len__()):
    z = int(user_Input)
    print(i)
    if z / i == i:
        print("wah")


# if int(user_Input) > 1:

#
#     print(f"Value {i + 1} is a Prime Number")
# else:
#     print(f"Value {i + 1} is not a Prime Number")
