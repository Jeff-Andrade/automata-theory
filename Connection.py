class Connection:
  def __init__(self, next, char):
    self.char = char
    self.next = next
  def compare_input(self, input):
    return self.char == input
