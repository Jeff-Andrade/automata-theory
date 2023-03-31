from Node import Node
from Automaton import Automaton


class Parser:
    def __init__(self, file):
        self.data = self.parse_text(file)
        self.automaton = self.create_automaton()

    @staticmethod
    def parse_text(file):

        def parse_transition(data):
            data = data.split(":")
            data[1] = data[1].split(">")
            transfer_elements(data)

            return data

        def transfer_elements(data):
            transferData = data[1]
            del (data[1])
            for i in range(len(transferData)):
                data.append(transferData[i])
            return data

        with open(file, mode="r") as f:
            fileData = f.read()

        dic = {}

        fileData = fileData.split("#")
        fileData.pop(0)

        for i in range(len(fileData)):
            fileData[i] = fileData[i].split("\n")
            fileData[i].pop(-1)
            dic[fileData[i][0]] = fileData[i][1:]


        for i in range(len(dic["transitions"])):
            dic["transitions"][i] = parse_transition(dic["transitions"][i])

        return dic

    def create_automaton(self):

        nodes = {}

        def create_states():
            states = self.data["states"]
            accepting = self.data["accepting"]
            for i in range(len(states)):
                node = Node(name=states[i],
                            accepting=(states[i] in accepting))
                nodes[states[i]] = node

        def create_transitions():
            transitions = self.data["transitions"]
            for i in range(len(transitions)):
                nodes[transitions[i][0]].connect_nodes(nodes[transitions[i][2]], transitions[i][1])

        def create_initial():
            initial = self.data["initial"]
            return nodes[initial[0]]

        create_states()
        create_transitions()

        return Automaton(create_initial())

    def get_automaton(self):
        return self.automaton
