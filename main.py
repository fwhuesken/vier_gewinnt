import os
import sys

player1 = "\033[1;32mPlayer 1\033[0;37m"
player2 = "\033[1;31mPlayer 2\033[0;37m"
symbol1 = "\033[1;32mX\033[0;37m"
symbol2 = "\033[1;31mO\033[0;37m"

"""
rowCount = 6
columnCount = 7 # max 9
board = []


def createBoard(rowCount, columnCount):
  baseRow = [""]
  row = [""]
  for i in range(columnCount):
    row.append("") # creates row with number of columns
    baseRow.append(i+1) # creates numbered row at the bottom
  for i in range(rowCount):
    board.append(row) # appends rows to board
  board.append(baseRow) # appends numbered row at the bottom
  #print(board)
  return(board)

board = createBoard(rowCount, columnCount)
print(board)
"""
def empty_board():
  board = [['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', 1, 2, 3, 4, 5, 6, 7]]
  return board

board = empty_board()

def pretty_print(board):
  print() 
  for row in board:
    for item in row:  
     print(f"{item:^1}", end=" | ")
    print("\n")
  print()

def announce_winner(player):
  print(f"{player} wins the game, whoop whoop!")
  print("\n Thank you for playing! Goodbye \n")
  sys.exit()

player = player1
symbol = symbol1
fullRows = []

def display_move(move, board, symbol):
  if board[1][move] != "": # first check if row becomes full with this move, than add move to board
      fullRows.append(move)
        
  for i in range(5,-1,-1): # 5 specifies number of rows, -1 is necessary so that 0 row can be reached, -1 indicates negative iteration
    if board[i][move] == "":
      board[i][move] = symbol
      return

def check_horizontal_win(board, symbol, player):
  count = 0
  for row in board:
    for i in range(len(row)):
      if row[i] == symbol:
        count += 1
        if count == 4:
          announce_winner(player)
      else:
        count = 0 # resets count to 0

def check_vertical_win(board, symbol, player):
  count = [0] * len(board[0])
  for sublist in board:
      for i in range(len(sublist)):
          if sublist[i] == symbol:
              count[i] += 1
              for row in count:
                if row == 4:
                  announce_winner(player)
          else:
            count[i] = 0

def check_diagonal_win(board, symbol, player):
    # Initialize counts to zero
    count = 0

    # Check diagonals starting from the top-left corner
    for i in range(len(board) - 3):
        for j in range(len(board[0]) - 3):
            for k in range(4):
                if board[i+k][j+k] == symbol:
                    count += 1
                    if count == 4:
                      announce_winner(player)
               
            count = 0

    # Check diagonals starting from the top-right corner
    for i in range(len(board) - 3):
        for j in range(3, len(board[0])):
            for k in range(4):
                if board[i+k][j-k] == symbol:
                    count += 1
                    if count == 4:
                      announce_winner(player)

            count = 0
  

def change_player(player, symbol):
  if player == player1: 
    return player2, symbol2
  else:
    return player1, symbol1

pretty_print(board)

while True:
  nextMove = int(input(f"{player}, enter a column number: \n"))
  if nextMove not in fullRows:
    display_move(nextMove, board, symbol)
    os.system("clear")
    pretty_print(board)
    
    check_horizontal_win(board, symbol, player)
    check_vertical_win(board, symbol, player)
    check_diagonal_win(board, symbol, player)
    player, symbol = change_player(player, symbol)

  else:
    print(f"Row {nextMove} is full, please choose a different row\n")
