# Game show simulator
print("Welcome to the Game Show!\nThere are three doors and behind one of them is a car.")
from random import randint
i = 0
Win = 0
Loss = 0
Yeswin = 0
Nowin = 0
Yesloss = 0
Noloss = 0
Guess = input("Which door do you guess? Or type 'Exit' to quit. ")
while Guess != "Exit":
    if Guess == 'Data':
        print("Total Wins, Losses", Win, Loss)
        print("Wins, Losses when switched:", Yeswin, Yesloss)
        print("Wins, Losses when not switched:", Nowin, Noloss)
        exit()
    i = i + 1
    Car = str(randint(1,3))
    Other = str(randint(1,3))
    while Other == Car or Other == Guess:
        Other = str(randint(1,3))
    print("We're going to reveal one losing door for you!", Other)
    Answer = str(input("Would you like to switch doors? (Yes or No)"))
    if Answer == 'Yes':
        Guessnew = str(randint(1,3))
        while Guessnew == Guess or Guessnew == Other:
            Guessnew = str(randint(1,3))
        if Car == Guessnew:
            print("Congratulations, you've won a new car!\n")
            Win = Win + 1
            Yeswin = Yeswin + 1
        elif Car != Guessnew:
            print("Sorry you're a loser!\n")
            Loss = Loss + 1
            Yesloss = Yesloss + 1
    else:
        Guessnew = Guess
        if Car == Guessnew:
            print("Congratulations, you've won a new car!\n")
            Win = Win + 1
            Nowin = Nowin + 1
        elif Car != Guessnew:
            print("Sorry you're a loser!\n")
            Loss = Loss + 1
            Noloss = Noloss + 1
    Guess = input("Lets start again. Which door or type 'Exit' to quit. ")
