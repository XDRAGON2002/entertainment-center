
# - THIS IS A GUESSING GAME

def GUESS():

    import random
    MyVar = random.randint(1 , 10)
    MyOpt = int(input("ENTER GUESS - "))


    while MyOpt != MyVar :

        if MyOpt > MyVar :
            print("GUESS LOWER ! ")
            MyOpt = int(input("ENTER GUESS - "))

        elif MyOpt < MyVar :
            print("GUESS HIGHER ! ")
            MyOpt = int(input("ENTER GUESS - "))

        else :
            print("INVALID INPUT ! ")

    else :
        print("YOU WIN ! ")
                
GUESS()
