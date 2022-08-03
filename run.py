
def create_boards():
    """ 
    generates the boards for both player and comupter
    """
    print("your board")
    row = 5
    col = 5
    for i in range(row):
        for j in range(col):
            print(" . ", end="")
        print()

    print("computer's board")
    for i in range(row):
        for j in range(col):
            print(" . ", end="")
        print()        



def new_game():

    """
    gives and introduction to the player and creats the board with randome 
    ships ready to play the game
        """
    print("welcome to battle ships supreame")
    player_name = input("please enter your name\n")
    print(f"welcome {player_name} get ready for some battleship warfare!!!\n")
    print(f"{player_name}'s battle felid")

    create_boards()


new_game()



    
    

