import random


def create_player_board():
    """
    adds the board and ships for the player
    """
    row = ["A", "B", "C", "D", "E"]
    colunm = 1, 2, 3, 4, 5
    players_grid = []
    for letter in row:
        for number in colunm:
            newElement = letter+str(number)
            players_grid.append(newElement)
            
    num_replacements = 4 
    idx = random.sample(range(len(players_grid)), num_replacements)
    for i in idx:
        players_grid[i] = '*'
            
    print(players_grid)    
       

def create_computer_board():
    """
    adds the board and ships for the computer
    """
    row = ["A", "B", "C", "D", "E"]
    colunm = 1, 2, 3, 4, 5
    computers_grid = []
    print("computer's battlefield")
    for letter in row:
        for number in colunm:
            newElement = letter+str(number)
            computers_grid.append(newElement)
    print(computers_grid)
    computer_ships = random.choices(computers_grid, 4)  
    print(computer_ships) 
    
         
def new_game():

    """
    gives and introduction to the player and creats the board with randome 
    ships ready to play the game
        """
    print("welcome to battle ships supreame")
    player_name = input("please enter your name\n")
    print(f"welcome {player_name} get ready for some battleship warfare!!!\n")
    print(f"{player_name}'s battle felid")
    
    create_player_board()
    create_computer_board()
    

new_game()

       
    




    
    

