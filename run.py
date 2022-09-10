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

    player_ships = (random.sample(players_grid, 4))
    print()

    print(f"your ships {player_ships}")
    print()

    print(players_grid)
    print()

    row = ["A", "B", "C", "D", "E"]
    colunm = 1, 2, 3, 4, 5
    computers_grid = []
    computer_ships = []
    print("computer's battlefield")
    for letter in row:
        for number in colunm:
            newElement = letter+str(number)
            computers_grid.append(newElement)
    print()
    print(computers_grid)

    computer_ships = (random.sample(computers_grid, 4))

    play_game(computers_grid, computer_ships, players_grid, player_ships)


def play_game(computers_grid, computer_ships, players_grid, player_ships):
    computer_num = 4
    player_num = 4

    print()
    print("pick a space on the board")
    print("the space has to be letter from A-E followed by a number from 1-5")
    print()
    while computer_num or player_num > 0:

        player_pick_space = input("pick a space on the board it has:\n")
        player_pick_space = player_pick_space.capitalize()

        while player_pick_space not in computers_grid:
            print("this is an invalid number try again")
            player_pick_space = input("pick a space on the board it has:\n")
            player_pick_space = player_pick_space.capitalize()

        if player_pick_space in computers_grid:
            print(f"you picked {player_pick_space}")

            if player_pick_space in computer_ships:
                print()
                print("YOU HIT")

                print()

                computer_num = computer_num - 1
                computers_grid = [s.replace(player_pick_space, " x") for s in computers_grid]
            else:
                print()
                print("YOU MISS")

                print()
                computers_grid = [s.replace(player_pick_space, " x") for s in computers_grid]
        else:
            print("this is an invalid number try again")
            

        print("computer's battlefield")

        print(computers_grid)

        print()
        print("computer's turn")

        print()
        print(f"the computer has {computer_num} ships remaining")

        print()

        computer_pick_space = random.choice(players_grid)
        while computer_pick_space == " x":
            computer_pick_space = random.choice(players_grid)
        
        if computer_pick_space != " x ":
            print(f"the computer picked {computer_pick_space}")
            print("------------")
            print()
            if computer_pick_space in player_ships:
                print("COMPUTER HIT")
                player_num = player_num - 1

                print(f"you have {player_num} ships remaining")

            else:
                print("COMPUTER MISS")
                print(f"you have {player_num} ships remaining")
        else:
            computer_pick_space = random.choice(players_grid)
            print(f"the computer picked {computer_pick_space}")
            print("------------")
            print()
            if computer_pick_space in player_ships:
                print("COMPUTER HIT")
                player_num = player_num - 1

                print(f"you have {player_num} ships remaining")

            else:
                print("COMPUTER MISS")
                print(f"you have {player_num} ships remaining")

        players_grid = [s.replace(computer_pick_space, " x") for s in players_grid]

        print()

        print(f"your ships {player_ships}")
        print()
        print("your battlfelid")
        print(players_grid)

        if computer_num == 0:
            print("CONGRATULATIONS YOU WON.THANK YOU FOR PLAYING MY BATTLES SHIPS GAME")
            play_again = input("would you like to play again (y/n)")

            if play_again == "y":
                create_player_board()
            else:
                print("Thank You for Playing")
                break
        if player_num == 0:
            print("NOOOOOOO YOU LOST. YOU FOR PLAYING MY BATTLES SHIPS GAME")
            play_again = input("would you like to play again (y/n)")

            if play_again == "y":
                new_game()
            if play_again == "n":
                print("Thank You for Playing")
                break
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
    print()
    print("your goal is to destroy the the ships on the enermy battle feild")
    print("before the computer destroys the ships on your battlefeild")
    print("the 1st player to destroy all battle ships wins ")
    print()
    print("GOOD LUCK!!!!")
    print()
    player_name = input("please enter your name:\n")
    print(f"welcome {player_name} get ready for some battleship warfare!!!\n")
    print(f"{player_name}'s battle felid")

    create_player_board()


new_game()

