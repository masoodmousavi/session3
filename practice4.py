user_input = int(input("enter: "))

for i in range(user_input):
    if i % 2 == 0:
        print("*", end = "")
    else:
        print("#", end = "")