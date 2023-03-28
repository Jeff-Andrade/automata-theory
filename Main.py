from Parser import Parser

parser = Parser("input-example.txt")
automaton = parser.get_automaton()

print(automaton.accepts_word("ccaaccaa"))
automaton.print_path()

print("\n")
