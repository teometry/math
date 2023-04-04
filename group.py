
class Group:
    def __init__(self, elements, operation):
        self.elements = elements
        self.operation = operation

    def multiply(self, g, h):
        for triple in self.operation:
            if triple[0] == g and triple[1] == h:
                return triple[2]

    def pow(self, x, n):
        a = 0
        for i in range(n):
            a = self.multiply(a,x)
        return a

    def deg(self, element):
        degree = 0
        while True:
            if self.pow(element, degree) == 0:
                break
            degree += 1
        return degree


elements = [0, 1, 2]
operation = []
for i in elements:
    for j in elements:
        result = [i, j]
        result.append((i+j)%len(elements))
        operation.append(result)

G = Group(elements, operation)
print(G.deg(1))
