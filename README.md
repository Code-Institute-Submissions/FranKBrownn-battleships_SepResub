# my battlships game
## functions
the game uses python only to bring a basic game of battleships to be played on the terminal. both the player and the AI have a genereated game "grid" from A1 through A5 following though the letters and number to finally reach E5 creat a grid with 25 postions on it. 

the ships and then placed on the grid and each player has 4 ships. the human player is able to see where his ships are postioned through a list which pops up at the begining of the human players move. the AI ships are hidden in a ist that was not printed to the terminal. 

## playing the game. 

playing the game is simple the play picks a tyle by typing in on sring for example "C3"
the terminal then tells the player if it is a hit or a miss and then that postion is then turned into an "X" to show to the player which tyles they have already attacked. 

the Ai then also takes his turn. folling a similer methored execpt his number is chosen wiht a random.choice method other then that the rules are almost the same.

once the game is compleate the player will be asked if they would like to play again with a y/n input answer


## issure i had along the way. 
i found this project the hardest so far not having an HTML and CSS file to fall back on and make it look nice and pretty was chalanging for me. i wish i could have made the terminal a bit more presentable. for example i wish i could have found a way to get the "grid" into a proper grid shape with a 5 x 5 ratio so it would be more readable to the user. 
 
## this i would like to improve
the grid is one that i metioned i would also like a way to clear the terminal after every move but i couldnt find a possible way of doing that mid game. clearing the terminal would make it alot easier for the user to read it and follow the scores and where their and the computers gids are. 

## bugs
i have spotted to bugs with in my code.

1. for some unknown reason and it only happens now and again when the game has ended and one side has won, during the point where the player is asked to play again some time when click n for no the player will be booted back a little bit to do the last turn again for promting the question again so the player can exit properly. 

2. during the game the players grid gets filled up with xs from where the AI has previously attack this can cause a problem because the AI randomises the next attack based on that new list mean somtimes the AI will attack with an X instead of a legel move. to reduce the chances of this happening i added a if != " x " else: the else stament had the code to make the AI pick is turn again before making the attack. this has not fixed the porblem but it help reduce it by a big margin as the AI now has a 2nd chance to guess right. 



