import random
def guessing_game():
    a = random.randint(1, 10)

    while True:
        b = int(input("Enter the guessed number:"))
        
        if b == a:
            print("You won the game :)")
            break
        elif b > a:
            print("Its greater than what computer as guessed")
        else:
            print("Its lesser than what computer says")

guessing_game()   