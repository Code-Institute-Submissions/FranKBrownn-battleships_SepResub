import random


def create_player_board():
    
    """
    adds the board and ships for the player
    """
    row = ["A", "B", "C", "D", "E"]
    colunm = 1, 2, 3, 4, 5
    players_grid = []
    player_ships = []
    for letter in row:
        for number in colunm:
            newElement = letter+str(number)
            players_grid.append(newElement)

    num_replacements = 4 
    idx = random.sample(range(len(players_grid)), num_replacements)
    for i in idx:
        players_grid[i] = '@'
    
    print(players_grid)  

    #computer

    row = ["A", "B", "C", "D", "E"]
    colunm = 1, 2, 3, 4, 5
    computers_grid = []
    computer_ships = []
    print("computer's battlefield")
    for letter in row:
        for number in colunm:
            newElement = letter+str(number)
            computers_grid.append(newElement)
    print(computers_grid)
    
    computer_ships = (random.sample(computers_grid, 4))  

    print(computer_ships) 

    play_game(computers_grid, computer_ships, players_grid,  player_ships)   


def play_game(computers_grid, computer_ships, players_grid,  player_ships):
    computer_num = 4
    player_num = 4
  
    print("pick a space on the board")
    print("the space has to be letter from A-E followed by a number from 1-5")
    while computer_num or player_num > 0:
        #players turn
        player_pick_space = input("pick a space on the board it has ")
        player_pick_space = player_pick_space.capitalize()
    
        if player_pick_space in computers_grid:
            print(f"you picked {player_pick_space}")
        
            if player_pick_space in computer_ships:
                print("HIT")
                print("------------")
                print()
    
                computer_num = computer_num - 1
            
            else:
                print("MISS")
                print("------------")
                print()
    
        else:
            print("this is an invalid number try again")

        
    
        computers_grid = [s.replace(player_pick_space, " x ") for s in computers_grid]  

        print(computers_grid)
        print("------------")
        print()
        print("computer's turn")
        print("------------")
        print()
        print(f"the computer has {computer_num} ships remaining")
        print("------------")
        print()
    
        #computers turn
        
        computer_pick_space = random.choice(players_grid)
        print(f"the computer picked {computer_pick_space}")
        print("------------")
        print()
        if player_pick_space == e2:
            print("HIT")
        else:
            print("MISS")    

        


        if computer_num == 0:
            print("CONGRATULATIONS YOU WON.THANK YOU FOR PLAYING MY BATTLES SHIPS GAME")
            play_again = input("would you like to play again (y/n)")
            
            if play_again == "y":
                create_player_board()
            else:
                print("Thank You for Playing") 
                break   

        else:
            continue   

        

    

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
    

new_game()

       


    
    
    

