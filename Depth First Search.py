from collections import defaultdict

class Graph:

    def _init_(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def helper(self, u, d, visited, path):
        visited[u] = True
        path.append(u)

        if u == d:
            print(path)
        else:
            for i in self.graph[u]:
                if visited[i] == False:
                    self.helper(i, d, visited, path)

        path.pop()
        visited[u] = False

    def printPaths(self, s, d):
        visited = [False] * (self.V)
        path = []
        self.helper(s, d, visited, path)

g = Graph(4)
g.addEdge(1, 1)
g.addEdge(0, 2)
g.addEdge(2, 2)
g.addEdge(2, 3)
g.addEdge(3, 3)
print("Please Enter any two vertices : ")
s = int(input())
d = int(input())
print("The Different paths exist from % d to % d are:" % (s, d))
g.printPaths(s, d)
