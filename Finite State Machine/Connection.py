class Connection:
    def __init__(self, next_, char):
        self.char = char
        self.next = next_

    def compare_input(self, input_):
        return self.char == input_
