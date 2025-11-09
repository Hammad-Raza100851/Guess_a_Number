#guess a number b/w 1 to 100
def game() : 
    import random
    a = random.randint(1,100)
    low = 1
    high = 100
    guess1 = 1
    b = -1 
    while a != b :
        b = int(input(f"Guess a number between {low} to {high} : " ))
        if a > b :
            print("To Low !")
            low = b+1
            guess1 += 1
        elif a < b :
            print("To High !")
            high = b-1
            guess1 += 1

    print(f"You guessed the number {a} in {guess1} guesses!")
    return guess1



print("First player turn")
a = game()
print("\nSecond player turn")
b = game()
if a>b:
    print("Second player Won :) ")
else :
    print("First player Won :) ")