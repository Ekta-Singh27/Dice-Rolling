import random
from pprint import pprint

def main():
    print("Welcome to Dice Rolling")    

    #Choose number of dices to play and display the rules for chosen number of dices
    dice = int(input("Number of dices : 1 or 2"))
    dice = rules(dice)

    #Number of players in a game
    no_of_players = int(input("Number of players: "))

    #game_history dict = {player{chance number : points gained}}
    game_history = {}

    #Names of the player and storing in the game_history dict
    print("Please enter below the names of the players:")
    for num in range(1,no_of_players+1):
        player_name = input(("Name of player #{}").format(num))
        game_history[player_name] = {}

    #Number of chances each player will have, skip if wanted indefinite number of chances
    try:
        no_of_chances = int(input("Number the chances each player will have (or Enter to skip) : "))
    except ValueError:
        no_of_chances = 0

    #players turn to roll the dice
    if(no_of_chances ==0): #when they chose indifinite number of chances
        play_again = "y"
        chance_count = 1
        while(play_again == "y"):
            for player in game_history.keys():
                print("{}'s Turn #{}".format(player, chance_count))                    
                game_history[player]["Turn #"+str(chance_count)] = play_rolling_dice(dice)
            play_again = (input("would you like to roll dice again?(Y/N)")).lower()
            if(play_again == "y"):
                chance_count +=1
    else: #Specific number of chances for each player
        for chance_count in range(1,no_of_chances+1):
            for player in game_history.keys():
                print("{}'s Turn #{}".format(player, chance_count))   
                game_history[player]["Turn #"+str(chance_count)] = play_rolling_dice(dice) 

    #Display game history for each player
    display_game_history = input("Would you like to see the game history?(Y/N)").lower()
    if(display_game_history == "y"):
        pprint(game_history, width = 1, indent = 1)
    print("Thanks for playing here. See you soon again")
    input("Press any key to exit")

    

#Roll dice and store the final dice total in dice_result_total
def play_rolling_dice(dice):
    dice_result_total = roll_dice(dice)
    print("dice_result_total = {}".format(dice_result_total))
    return dice_result_total


def rules(dice):
    if(dice == 1):
        print("""Rules for 1 dice
                    1. Each player will take their turn to roll the dice
                    2. If 6 comes, player will get another chance to roll the dice
                    3. Player can get upto two 6's in a row, and get the total points as sum of the numbers he got in each chance
                    4. If player got three 6's in row, the player forefeits their turn and get a Zero""")
    elif(dice==2):
        print("""Rules for 2 dices
                    1. Each player will take their turn to roll the dice
                    2. Player receives the total point as sum of numbers shown on both dices
                    3. If both dices shows same number, player will get another chance to roll the dice
                    4. Player can get upto two times same number on both dices in a row, and get the total points as sum of the numbers he got in each chance
                    5. If player got three times same number on both dices in row, the player forefeits their turn and get a Zero """)
    else:
        dice = int(input("Please choose again. Number of dices : 1 or 2"))
        rules(dice)
    return dice

def roll_dice(dice):
    input("Press enter to roll your dice.....")
    
    # Number of dices chosen was 1
    if(dice == 1):
        print("Rolling single dice")
        dice_result = random.randint(1,6)        
        
        if(dice_result==6):
            count = 1
            dice_result_final = dice_result
            while(dice_result==6 and count<=3):
                if(count==3):
                    print("Oh No, You got 3 times 6, you will get Zero")
                    dice_result_final = 0
                    break
                print("Hey it's a 6, you will get get another chance to roll")
                print("Chance Number #{}".format(count+1))
                input("Press enter to roll your dice again.....")
                dice_result = random.randint(1,6)
                dice_result_final += dice_result   
                count +=1             
        else:
            dice_result_final = dice_result         

        
    # Number of dices chosen was 1
    elif(dice == 2):
        print("Rolling double dice")
        dice1_result = random.randint(1,6)
        print("dice1_result {}".format(dice1_result))
        dice2_result = random.randint(1,6)
        print("dice2_result {}".format(dice2_result))
        dice_result = dice1_result + dice2_result

        if(dice1_result==dice2_result):
            count = 1
            dice_result_final = dice_result
            while((dice1_result==dice2_result) and count<=3):
                if(count==3):
                    print("Oh No, You got 3 times same number on both the dices, you will get Zero")
                    dice_result_final = 0
                    break
                print("Hey it's a same number on both the dices, you will get another chance to roll")
                print("Chance Number #{}".format(count+1))
                input("Press enter to roll your dice again.....")
                dice1_result = random.randint(1,6)
                print("dice1_result {}".format(dice1_result))
                dice2_result = random.randint(1,6)
                print("dice2_result {}".format(dice2_result))
                dice_result_final += dice1_result + dice2_result  
                count +=1             
        else:
            dice_result_final = dice_result      

    #Returning final total number from dice roll per chance  
    return dice_result_final



main()


