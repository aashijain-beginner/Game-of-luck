import random
#definig the dice working
def throw():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll
#checking the number of players to play the game
while True:
    players=input("Enter the number of players(2-4): ")
    if(players.isdigit()):
        players=int(players)
        if(2<=players<=4):
            break
        else:
                print("Must be beetween 2-4.")
    else:
            print("Invalid value,try again")
#storing players scores
max_score=30
player_score=[0 for _ in range(players)]
while max(player_score)<max_score:
    for player_idx in range(players):                                                                                       #idx represents the index 
        print("\n Player number",player_idx+1,"turn has started now !")
        print("Your total score is:",player_score[player_idx],"\n")
        current_score=0

        while True:
            should_roll=input("Would you like to roll(y/n)?")                                                        #y stands for yes and n stands for no
            if (should_roll.lower() !="y"):
                break
            value=throw()
            if(value==1):
                print("You rolled 1!,your turn is done")
                current_score=0
                print("Your score is: ",current_score)
                break
            else:
                current_score+=value
                print("You rolled a: ",value)
            print("Your score is: ",current_score)
        player_score[player_idx]+=current_score
    print("Your total score is: ",player_score[player_idx])

max_score=max(player_score)
winning_player=player_score.index(max_score)
print("\nPlayer number",winning_player+1,"is the winner with the score of: ",max_score)
