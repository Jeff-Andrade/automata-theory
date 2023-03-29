class Automaton:
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
        self.path.append(self.start.name)
        for char in code:
            self.choose_path(char)
            self.path.append(self.current.name)
        return self.current.isAccepting

    def print_path(self):
        for i in range(len(self.path)):
            print(self.path[i], end="")
            print(" -> ", end="")
            if i == len(self.path) - 1:
                print(self.path[i], end="")
