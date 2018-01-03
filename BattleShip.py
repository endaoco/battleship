#Battleship
#Enda O'Connell

from random import randint

###############################
#Printing the board #
###############################
board = []
good_board = []

board_numbers = [['0', '1', '2', '3', '4']]

for x in range(0, 5):
  board.append(["~"] * 5)
  good_board.append(["~"] * 5)

number_col = 0
for row in board:
  row.insert(0, "|")
  row.insert(0, str(number_col))
  number_col += 1

number_col = 0
for row in good_board:
  row.insert(0, "|")
  row.insert(0, str(number_col))
  number_col += 1

def print_board(board):
  print("    0 1 2 3 4")
  print(("   "), "- " * 5)
  for row in board:
    print(" ".join(row))

def print_both_boards():
  print_board(board)
  print(("   "), "= " * 5)
  print_board(good_board)

###############################
#Setting up the game#
###############################

player_ship_row = int(input("Choose row for your ship: "))
player_ship_col = int(input("Choose column for your ship: ")) + 2

good_board[player_ship_row][player_ship_col] = "O"

print_both_boards()

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(2, len(board) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

###############################
#Playing the game #
###############################
comp_win = False
player_win = False
game_bool = True

while(game_bool):
  #player go
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: ")) + 2

  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sank my battleship!")
    game_bool = False
    player_win = True
  else:
    if guess_row not in range(5) or \
      guess_col not in range(7):
      print("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"

  #comp go
  comp_row_guess = random_row(good_board)
  comp_col_guess = random_col(good_board)
  print(("row:"),comp_row_guess)
  print(("col:"),comp_col_guess)
  if comp_row_guess == player_ship_row and comp_col_guess == player_ship_col:
    game_bool = False
    comp_win = True
  else:
    good_board[comp_row_guess][comp_col_guess] = "X"
    print("I missed =(")
  print_both_boards()

if (player_win):
  print("You win you sank my battleship!")
else:
  print("You lose! I sank your battleship!")
