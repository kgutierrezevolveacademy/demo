#EvolveAcademy Lab: 31
#fruit_basket()
#Ken.Gutierrez
#9-22-18

fruit_basket = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    
print ("Please guess the fruit in the basket: ")
guess = str(input())

while not (guess in fruit_basket):
    print ("Guess again: " )
    guess = str(input())

#if (guess in fruit_basket):
print("You chose the right fruit! \n", guess, "is in the basket!")
#else:
#    print(guess, "is not in the fruit basket \n")


print ("Finished, Thanks for playing!")
