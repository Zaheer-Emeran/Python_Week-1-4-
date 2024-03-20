import random
import time

# The function should only return a string either:
# 50% of the time,
# 25% of the time, or
# 10% of the time.
# Must include a variable "Services are up. If True, generate chance of string. Else, no display string"
# The code:
# get_With_Retry should be called until it receives a not null string.
# After a certain period of time, give up
percentage = None
services_Are_Up = True

output_Message = lambda percentage: f"You got the data! That only happens {percentage}% of the time"


# Decides what percentage will be selected
def percentage_Decider():
    if random.random() > 0.5 :
        x = "50"
    elif random.random() > 0.25 :
        x = "25"
    elif random.random() > 0.1 :
        x = "10"
    else:
        x = "x"
    return x


for i in range(0, 20):
    temp = percentage_Decider()
    if temp != "x":
        print(percentage_Decider())
    else:
        time.sleep(3)
        print("System is Down ;-;")
        break

print(456 % 6)

# Dont forget to modify this code Zee
#         print(output_Message(percentage_Decider()))
