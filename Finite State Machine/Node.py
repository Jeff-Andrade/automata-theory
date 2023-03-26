from Connection import Connection

class Node:
  def __init__(self, name, isAccepting=False):
    self.connections = []
    self.name = name
    self.isAccepting = isAccepting
  def connect_nodes(self, node, char):
    connection = Connection(node, char)
    self.connections.append(connection)
