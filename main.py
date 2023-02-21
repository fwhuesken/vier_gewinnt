import os
player1 = "Player 1"
player2 = "Player 2"

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

player = player1
symbol = "X"

def addMoveToBoard(nextMove, board, symbol):
  for i in range(5,-1,-1):
    if board[i][nextMove] == "":
      board[i][nextMove] = symbol
      return
    """
    elif board[i][nextMove] != "":
      print("Column full, please choose a different column")
    """

while True:
  os.system("clear")
  prettyPrint(board)
  nextMove = int(input(f"{player}, enter a column number > "))
  
  addMoveToBoard(nextMove, board, symbol)
  
  if player == player1: 
    player = player2
    symbol = "O" # specify symbol on board for player1
  else:
    player = player1 # switch players for next round
    symbol = "X" # specify symbol on board for player1