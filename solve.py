class Link:
  def __init__(self, fst, snd):
    self.cells = [fst, snd]
    self.value = 0
    self.editable = True

    self.conflicts = []

  def freeze(self):
    self.editable = False

  @property
  def available(self):
    if self.editable:
      return 2 - self.value
    else:
      return 0

  def inc_link(self):
    assert self.editable, "Bridge cannot be edited"
    assert self.available > 0, "Bridge already at max"
    for c in self.conflicts:
      assert c.value == 0, "A cross-bridge already exists"

    self.value += 1
    for c in self.conflicts:
      c.freeze()


class Cell:
  def __init__(self, val, row, col):
    self.val = val
    self.row = row
    self.col = col

    self.links = []

  def add_link(self, link):
    self.links.append(link)

  @property
  def n_links(self):
    return sum(l.value for l in self.links)

  @property
  def done(self):
    return self.val == self.n_links

  @property
  def needed(self):
    return self.val - self.n_links

class Board:
  def __init__(self):
    self.cells = []
    self.links = []
    pass

  def add_cell(self, val, row, col):
    self.links.append(Cell(val = val, row = row, col = col))

  def add_bridges(self):
    pass

  @property
  def cells(self):
    yield None
    pass

  def __str__(self):
    row_strings = [" ".join([str(x) for x in row]) for row in puzzle]
    return "\n".join(row_strings)

def task_to_puzzle(task_string, width, height):
  # Init variables
  islands = [[" " for y in range(height)] for x in range(width)]
  counter = 0

  # Create islands
  for c in task_string:
    # If digit, place island there
    if c.isdigit():
      row = counter // width
      col = counter  % width
      value = int(c)

      board.add_cell(value, row, col)
      islands[row][col] = Cell(value, row, col)
    # If not, increment our counter...
    else:
      inc = ord(c) - ord('a') # a: +0, b: +1, ...
      counter += inc
    counter += 1







if __name__ == "__main__":
  #task_string = input()
  task_string = "3a5b4g2c2a3a3j2a6c2a1a4a4c3"
  task_to_puzzle(task_string, width = 7, height = 7)
