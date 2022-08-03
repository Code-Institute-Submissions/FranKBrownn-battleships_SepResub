from random import randint

scores = {"computer": 0, "player": 0}

class board:

    """
    the board where the game is played by adding the number of ships to random 
    postions, players name to both the player and the computer
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        for row in self.board:
            print(" ".join(row))   

    def guess(self, x, y):
        self.guesses.append(x, y)    
        self.board[x] [y] = "x"

        if (x, y) in self.ships:
            self.board[x] [y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, y, type="AI"):
        if len(self.ships) >= self.num_ships:
            print("Error max number of ships reached")     
        else:
            self.ships.append((x, y))      
            if self.type == "player":
                self.board [x] [y] ="@"    

def random_point(size):
    """
    creats a random number between 0 and the size of the board
    """             
    return randint(0, size - 1)

def new_game():
    """
    starts a new game restarting all scores and reseting ship postions
    """
    size = 5
    num_ships = 4
    scores["AI"] = 0
    scores["player"] = 0
    print("-" * 35)
    print("welcome to battleships supreme")
    print(f"board size: {size}. number of ships: {num_ships}")
    print("top left corner is row: 0  col: 0")
    print("-" * 35)
    player_name = input("please enter your name: \n")
    print("-" * 35)

new_game()        





