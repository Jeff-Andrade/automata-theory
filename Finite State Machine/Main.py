from Parser import Parser

parser = Parser("input-example.txt")
automaton = parser.get_automaton()

print(automaton.accepts_word("abbabbaaa"))
automaton.print_path()
