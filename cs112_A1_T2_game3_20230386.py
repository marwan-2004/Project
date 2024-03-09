#file name:cs112_A1_T2_20230386
#purpose:subtract a square number like (4,9,16,25,..) and the one who reach zero wins
#Author:marwan maged maher
#ID:20230386


from random import randint

def is_sqr(n):
    """
    check if the number is a square
    n:the number to be checked
    return:boolean
    """

    i=1
    while i * i < n:
        i+=1
    return True if i*i == n else False

def valid_move(x, n):
    """
    check if move x is possible
    :param x: player input
    :param n: current number of coins
    :return: boolean
    """

    return True if is_sqr(x) and x<= n else False

def main_loop():
    """
    Main loop function of the game
    :return:none
    """
    #this make sure that the starting number of coins is random
    coins=randint(10,1000)

    cur_player=False
    player_name={False: "player 1",True: "player 2"}
    while coins>0:
        print("current number of coins",coins)

        try:
            player_input=int(input(f"{player_name[cur_player]}'s Turn:"))
        except ValueError:
            print("Invalid move")
            continue

        if valid_move(player_input,coins):
            coins-=player_input
            if coins !=0:
                #change player after each move

                cur_player=not cur_player
        else:
            print("Invalid move")
    print(player_name[cur_player],"wins!")

if __name__=="__main__":
    reset ="y"
    while reset == "y":
        main_loop()
        reset =input("want to play again? y/n:").lower()
    else:
        print("Goodbye")
