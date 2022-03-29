def valid_row(row, grid):
  temp = grid[row]
  temp = list(filter(lambda a: a != 0, temp))
  if any(i < 0 and i > 9 for i in temp):
    print("Invalid value")
    return -1
  elif len(temp) != len(set(temp)):
    return 0
  else:
    return 1
def valid_col(col, grid):
  temp = [row[col] for row in grid]
  temp = list(filter(lambda a: a != 0, temp))
  if any(i < 0 and i > 9 for i in temp):
    print("Invalid value")
    return -1
  elif len(temp) != len(set(temp)):
    return 0
  else:
    return 1
def valid_subsquares(grid):
  for row in range(0, 9, 3):
      for col in range(0,9,3):
         temp = []
         for r in range(row,row+3):
            for c in range(col, col+3):
              if grid[r][c] != 0:
                temp.append(grid[r][c])
         if any(i < 0 and i > 9 for i in temp):
             print("Invalid value")
             return -1
         elif len(temp) != len(set(temp)):
             return 0
  return 1

def valid_board(grid):
  
  for i in range(9):
      res1 = valid_row(i, grid)
      res2 = valid_col(i, grid)
      
      if (res1 < 1 or res2 < 1):
          print("no")
          return
  
  res3 = valid_subsquares(grid)
  if (res3 < 1):
      print("no")
  else:
      print("yes")
def print_board(grid):
  for row in grid:
    print(row)
board = [[2,9,5,7,4,3,8,6,1],
        [4,3,1,8,6,5,9,2,7],
        [8,7,6,1,9,2,5,4,3],
        [3,8,7,4,5,9,2,1,6],
        [6,1,2,3,8,7,4,9,5], #if we will change any number example 6 to 1 it will output no
        [5,4,9,2,1,6,7,3,8],
        [7,6,3,5,2,4,1,8,9],
        [9,2,8,6,7,1,3,5,4],
        [1,5,4,9,3,8,6,7,2]]
valid_board(board)
