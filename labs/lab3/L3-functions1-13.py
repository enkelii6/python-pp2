import random as r
def Game():
    name = input("Hello! What is your name? ")
    b = r.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    i = 0
    while True:
        i += 1
        print("Take a guess")
        c = int(input())
        if c == b:
            print(f"Good job, {name}! You guessed my number in {i} guesses!")
            break
        elif c > b:
            print("Your guess is too big")
            continue
        else:
            print("Your guess is too low")
            continue

Game()