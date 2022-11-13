import random

sc1 = 0
sc2 = 0
print("Welcome to Rock-Paper-Scissors")
print("I will be the one you will be playing against!")
print('''*******DISCLAIMER*******''')
print("Please type your choices as: Rock,Paper or Scissors")
print("Dont type rock, paper or scissors")


while True:
    a = ['Rock', 'Paper', 'Scissors']
    b = random.choices(a, k=1)
    comp = b[0]

    if sc1 == 3:
        print('''
        **Final Scores**
        YOU-''', sc1,'''
        COMP-''', sc2)
        print("You WIN")
        break
    elif sc2 == 3:
        print("You LOSE")
        print('''
                **Final Scores**
                YOU-''', sc1, '''
                COMP-''', sc2)
        break
    else:
        pass

    user = input("Enter your Choice: ")

    if user == 'Rock' and comp == 'Scissors':
        print("The computer chose ",comp)
        print("You have won")
        sc1 += 1
    elif user == 'Rock' and comp == 'Paper':
        print("The computer chose ",comp)
        print("You have lost")
        sc2 += 1
    elif user == 'Rock' and comp == 'Rock':
        print("SAME SHIT! Retry")
    elif user == 'Scissors' and comp == 'Rock':
        print("The computer chose ",comp)
        print("You have lost")
        sc2 += 1
    elif user == 'Scissors' and comp == 'Scissors':
        print("SAME SHIT! Retry")
    elif user == 'Scissors' and comp == 'Paper':
        print("The computer chose ",comp)
        print("You have won")
        sc1 += 1
    elif user == 'Paper' and comp == 'Scissors':
        print("The computer chose ",comp)
        print("You have lost")
        sc2 += 1
    elif user == 'Paper' and comp == 'Rock':
        print("The computer chose ",comp)
        print("You have won")
        sc1 += 1
    elif user == 'Paper' and comp == 'Paper':
        print("The computer chose ",comp)
        print("SAME SHIT! Retry")
    else:
        print("Give a correct input!")


