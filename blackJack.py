def sumMoreThan21(play):
    for i in play:
        sum=sum+i
    return sum
    # if sum>21:
    #     print("you lose")
    # if sum<=17:
    #     print("Sum is less than 17 pick up one more card")
"""
import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
computer=[random.choice(cards)]
print(f"computer cards is {computer}")
computer.append(random.choice(cards))
player=[random.choice(cards)]
player.append(random.choice(cards))
print(f"player cad is {player}")
y=True
while y:
    sumP=sumMoreThan21(player)
    sumC=sumMoreThan21(computer)
    print(f"sum of all your cards is {sumP}")
    if sumP>21:
        print("you lose")
        y=False
    elif sumC>21:
        print(f"sum of all computer cards is {sumC}")
        print("You Win")
    elif sumP<=17:
        print("pick one more card")

"""
import random
gameOver=False
def dealCard():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(userScore,computerscore):
    if userScore==computerScore or (computerScore>21 and userScore>21):
        return "draw"
    elif userScore==0:
        return "You win with Blackjack"
    elif computerScore==0:
        return "You Lose Opponent has Blackjack"
    elif computerScore>21:
        return "You win1"
    elif userScore>21:
        return "You lose1"
    elif computerScore>userScore:
        return "You Lose2"
    else:
        return "You Win2"
userCard=[]
computerCard=[]
for i in range(2):
    userCard.append(dealCard())
    computerCard.append(dealCard())
print(userCard,computerCard)
while not gameOver:
    userScore=score(userCard)
    computerScore=score(computerCard)
    print(f"your cards: {userCard},current Score is {userScore}")
    print(f"Computer card: {computerCard[0]}")
    if userScore==0 or  computerScore==0 or userScore>21:
        gameOver=True
    else :
        userAns=input("type y for another card or n to pass")
        if userAns.lower()=="y":
            userCard.append(dealCard())
        else:
            gameOver=True
while computerScore!=0 and computerScore<17:
    computerCard.append(dealCard())
    computerScore=score(computerCard)
    print(f"computerScore{computerScore}")
print(f"Your final hand: {userCard}, final score: {userScore}")
print(f"Computer final cards: {computerCard}, final Score:{computerScore}")
print(compare(userScore,computerScore))
