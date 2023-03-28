class Automaton():
  def __init__(self, start):
    self.start = start
    self.current = start
    self.path = []
  def choose_path(self, char):
    for connection in self.current.connections:
      if connection.compare_input(char):
        self.current = connection.next
  def accepts_word(self, code):
    self.path.clear()
    self.current = self.start
    for char in code:
      self.choose_path(char)
      self.path.append(self.current.name)
    return self.current.isAccepting
  def print_path(self):
    for node in self.path:
      print(node)
