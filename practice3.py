a = []
b = True
for i in range(5):
    user_input = int(input("enter your number: "))
    a.append(user_input)        

#for i in range(4):

    #if a[i] < a[i+1]:
        #b = True

    #if a[i] < a[4]:
        #b = True    

    #else:
        #b = False


if a[0] < a[1] and a[1] < a[2] and a[2] < a[3] and a[3] < a[4]:
    print("this list is sort")

else:
    print("this list is not sort")    
