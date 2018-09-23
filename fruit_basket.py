#EvolveAcademy Lab: 31
#fruit_basket()
#Ken.Gutierrez
#9-22-18

def guess_fruit(guess):
    fruit_basket = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    return (guess in fruit_basket)



def main():
    i = 1
    
    print ("Please guess the fruit in the basket: ")
    guess = str(input())

    inBasket = guess_fruit(guess)
    while not (inBasket) and i < 5:
        print ("Guess again: " )
        guess = str(input())
        i += 1

    if (inBasket):
        print("You chose the right fruit! \n", guess, "is in the basket! \n")
    else:
        print(guess, "is not in the fruit basket \n")

    print ("Finished, Thanks for playing!")

main()

