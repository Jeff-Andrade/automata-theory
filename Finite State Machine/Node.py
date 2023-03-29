from Connection import Connection


class Node:
    def __init__(self, name, accepting=False):
        self.connections = []
        self.name = name
        self.isAccepting = accepting

    def connect_nodes(self, node, char):
        connection = Connection(node, char)
        self.connections.append(connection)
