import random
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card= random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)

def compare(uscore,cscore):
    if uscore>21 and cscore>21:
        print("More! You Lose!")

    if uscore==cscore:
        return "Draw!!!"
    elif cscore==0:
        return "You Lose! Opponent has a blackjack!!!"
    elif uscore==0:
        return "You WIN!!! With a BlackJack"
    elif uscore>21:
        return "You LOSE! You went OVER!"
    elif cscore>21:
        return "You WIN! Opponent has went over!"
    elif uscore>cscore:
        return "You WIN!!!"
    else:
        return "You LOSE!!!"

def play_game():
    ucards=[]
    ccards=[]
    game_over = False

    for i in range(2):
        ucards.append(deal_card())
        ccards.append(deal_card())

    while not game_over:
        uscore=calculate_score(ucards)
        cscore=calculate_score(ccards)
        print(f" Your cards: {ucards}, Your Score: {uscore}")
        print(f" Opponent's First Card: {ccards[0]}")

        if uscore==0 or cscore==0 or uscore>21:
            game_over= True
        else:
            usd=input("Press 'y' if you want another card, 'n' for pass")
            if usd=='y':
                ucards.append(deal_card())
            else:
                game_over=True

    while cscore!=0 and cscore<17:
        ccards.append(deal_card())
        cscore=calculate_score(ccards)

    print(f"   Your final hand: {ucards}, final score: {uscore}")
    print(f"   Computer's final hand: {ccards}, final score: {cscore}")
    print(compare(uscore,cscore))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()


