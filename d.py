import random

class Node:
    def __init__(self, code):
        self.code = code

class Arc:
    def __init__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node

    def includesNode(self, node):
        b1 = self.from_node == node
        b2 = self.to_node == node
        if b1 or b2:
            return True
        return False

class Graph:
    def __init__(self, nodes, arcs):
        self.nodes = nodes
        self.arcs = arcs

    def deg(self, node):
        degree = 0
        for arc in self.arcs:
            if arc.includesNode(node):
                degree += 1
        return degree

nodes = [Node(i) for i in range(8)]
arcs = []
for node in nodes:
    for node1 in nodes:
        if random.randint(0,1):
            arcs.append(Arc(node, node1))

G = Graph(nodes, arcs)
print(G.deg(nodes[5]))
