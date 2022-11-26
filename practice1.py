import random

bank =["masoud","mohammad","amir","hasan","hosein","abbas","maryam","mahtab","zahra","fatemeh","sarvenaz","zeynab","roghayyeh","reza"]


user_miss_rate=0
winer = 0
true_chars = []
false_chars = []

word = random.choice(bank)


while user_miss_rate < 5:

        for i in range(len(word)):
            
            if word[i] in true_chars:
                print(word[i],end=" ")
                winer=winer+1

            else:
                print("_ ",end="")

        
        user_char = input("pls enter your character:")
        user_char.lower()

        if len(user_char)==1:

            if user_char in word:
                true_chars.append(user_char)
                print("✔")
            
            else:
                false_chars.append(user_char)
                print("✖")
                user_miss_rate = user_miss_rate+1    
            
        else:
            print("pls enter one character")        

if user_miss_rate == 5:
    print("kekbye losser")        