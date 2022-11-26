a = []

while True:

    user_input =int(input("enter your number:"))

    if user_input in a:
        print("this number in list!!!")

    else:
        a.append(user_input)


    print(a)