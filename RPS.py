import random
play_again='yes'
while play_again=='yes':
    choices=['rock','paper','scissor']
    computer=random.choice(choices)
    player=None
    player=input("rock,paper or scissor:").lower()
    if player in choices:
        print("computer:",computer)
        print("player:",player) 
        if player=='rock':
            if computer=="paper":
                print("you lose")
            elif computer=="scissor":
                print("You Win")
            else:
                print("Tie")
        elif player=='paper':
            if computer=="paper":
                print("Tie")
            elif computer=="scissor":
                print("You lose")
            else:
                print("You Win")
        elif player=='scissor':
            if computer=="paper":
                print("you Win")
            elif computer=="scissor":
                print("Tie")
            else:
                print("You lose")
    play_again=input("Play Again(yes/no):").lower()
    if play_again!='yes':
        break
    
print("Bye")
