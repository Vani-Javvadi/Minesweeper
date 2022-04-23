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
  #global grid
  if grid[r][c] == '*':
    return True



def placing_values_grid():
  global size
  global grid
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
      
      
  for row in grid:
    print("  ".join(str(cell) for cell in row))
    
   
if __name__ == "__main__":
  num_mines = 5
  size = 5
  grid = [[0 for row in range(size)] for col in range(size)]

place_mines_grid()
placing_values_grid()


