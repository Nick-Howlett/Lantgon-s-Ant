class Board:

  def __init__(self):
    self.board = [[False for i in range(11)] for j in range(11)]
    self.ant = Ant()
    
  def place_ant(self):
    self.board[self.ant.pos[0]][self.ant.pos[1]] = 'A'
  

  def take_turn(self):
    if self.board[self.ant.pos[0]][self.ant.pos[1]]:
      self.ant.turn(-1)
    else:
      self.ant.turn(1)
    self.board[self.ant.pos[0]][self.ant.pos[1]] = not self.board[self.ant.pos[0]][self.ant.pos[1]]
    self.ant.move()
    

  def print(self):
    for row in self.board:
      print("|".join(["B" if el else "W" for el in row])) 


class Ant:

  def __init__(self):
    self.pos = [5, 5]
    self.current_dir = 0
    self.direcs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

  def move(self):
    self.pos = [x + y for x, y in zip(self.pos, self.direcs[self.current_dir])]
    return self.pos
  
  def turn(self, turn):
    self.current_dir += turn
    self.current_dir %= 4
  


board = Board()
for i in range(100):
  board.print()
  board.take_turn()
