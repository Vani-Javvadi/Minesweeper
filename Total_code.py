#python 3.7.1

from random import randint

def place_mines_grid():
  global num_mines
  global size
  global grid 
  count = 0
  for count in range(num_mines):
    row = randint(0,size - 1)
    col = randint(0,size - 1)
    if grid[row][col] != '*':
      grid[row][col] = '*'
      count += 1     
  #for row in grid:
   # print("  ".join(str(cell) for cell in row))
  
  
def is_mine(grid,r,c):
  if grid[r][c] == '*':
    return True


def placing_values_grid():
  global size
  global grid
  global count1
  for row in range(size):
    for col in range(size):
      if grid[row][col] == '*':
        continue

      if row > 0 and is_mine(grid,row - 1,col):
        grid[row][col] += 1
        
      if row < size - 1 and is_mine(grid,row + 1,col):
        grid[row][col] += 1
        
      if col > 0 and is_mine(grid,row,col - 1):
        grid[row][col] += 1
        
      if col < size - 1 and is_mine(grid,row,col + 1):
        grid[row][col] += 1
        
      if row < size - 1 and col < size - 1 and is_mine(grid,row + 1,col + 1):
        grid[row][col] += 1
        
      if row > 0 and col > 0 and is_mine(grid,row - 1,col - 1):
        grid[row][col] += 1
        
      if row < size - 1 and col > 0 and is_mine(grid ,row + 1,col - 1): 
        grid[row][col] += 1
        
      if row > 0 and col < size - 1 and is_mine(grid ,row - 1,col + 1):
        grid[row][col] += 1
      
      count1 += 1
  for row in grid:
    print("  ".join(str(cell) for cell in row))
  print(f"Toatl values:{count1}")
    
   
def won_game(list_nonzeros):
  for value in list_nonzeros:
    print(value)
  print("congratulations ! you won the game")
  

def lose_game():
  for row in range(size):
    for col in range(size):
      if grid[row][col] == '*':
        print(grid[row][col])
  print("lose the game! u entered into a mine ")
         
   
 #3 types of inputs 
list_nonzeros = []

def input_types(grid,row_in,col_in):
  global flag
  global count1
  global count2
  if grid[row_in][col_in] != '*':
    if grid[row_in][col_in] == 0:
      print(grid[row_in][col_in])
      count2 += 1
    else:
      list_nonzeros.append(grid[row_in][col_in])
      if count1 - count2 == len(list_nonzeros):
        won_game(list_nonzeros)
  if grid[row_in][col_in] == '*':
    flag = 1
    lose_game()
 
 
def giving_input():  
  global flag
  if flag == 0:
    for row in range(size):
      for col in range(size):
        row_in,col_in = map(int,input("Enter row and column: ").split())
        input_types(grid,row_in,col_in)  
    
  
if __name__ == "__main__":
  flag = 0
  num_mines = 6
  size = 5
  count2 = 0
  count1 = 0
  grid = [[0 for row in range(size)] for col in range(size)]


place_mines_grid()
placing_values_grid()
giving_input()
 
