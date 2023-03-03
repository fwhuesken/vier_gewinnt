import os
import threading
import sys

player1 = "Player 1"
player2 = "Player 2"
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
"""

board = [['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', 1, 2, 3, 4, 5, 6, 7]]

def prettyPrint(board):
  print() 
  for row in board:
    for item in row:  
     print(f"{item:^1}", end=" | ")
    print("\n")
  print()

def announceWinner(player):
  print(f"{player} wins the game, whoop whoop!")
  sys.exit()

player = player1
symbol = symbol1

def addMoveToBoard(nextMove, board, symbol):
  for i in range(5,-1,-1): # 5 specifies number of rows, -1 is necessary so that 0 row can be reached, -1 indicates negative iteration
    if board[i][nextMove] == "":
      board[i][nextMove] = symbol
      return
    #else:
    #  print("Column full, please choose a different column")

def checkHorizontalWin(board, symbol, player):
  count = 0
  for row in board:
    for i in range(len(row)):
      if row[i] == symbol:
        count += 1
        if count == 4:
          announceWinner(player)
      else:
        count = 0 # resets count to 0

"""
def changePlayer(player, symbol):
  if player == player1: 
    player = player2
    symbol = symbol2 # specify symbol on board for player1
    print(player)
  else:
    player = player1 # switch players for next round
    symbol = symbol1 # specify symbol on board for player1
    print(player)
  return player, symbol
"""
prettyPrint(board)
while True:
 
  nextMove = int(input(f"{player}, enter a column number > "))
  addMoveToBoard(nextMove, board, symbol)
  os.system("clear")
  prettyPrint(board)
  
  checkHorizontalWin(board, symbol, player)
  #player = changePlayer(player, symbol)[0]
  #symbol = changePlayer(player, symbol)[1]
  

  if player == player1: 
    player = player2
    symbol = symbol2 # specify symbol on board for player1
  else:
    player = player1 # switch players for next round
    symbol = symbol1 # specify symbol on board for player1
