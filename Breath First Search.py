print("-----Salih - 12092-----")
vertexList=['0','1','2','3','4','5','6','7']
EdgeList=[(0,1),(0,2),(1,3),(1,4),(2,0),(2,5),(2,6),(3,1),(4,1),(4,7),(5,2),(6,2),(7,4)]
Graph=(vertexList,EdgeList)

AdjList=[[] for vertex in vertexList]
VisitedList=[]
n=[0 for ver in VisitedList]

def bfs(graph,start,end):
    n.insert(start,-1)
    vertexList,EdgeList = Graph
    queue=[start]
    
    for edge in EdgeList:
        AdjList[edge[0]].append(edge[1])
        print("So, here we have adjacency list : ",AdjList)
        while queue:
            current = queue.pop()
            
            for neighbor in AdjList[current]:
                if not neighbor in VisitedList:
                    queue.insert(0,neighbor)
                    n.insert(neighbor,cuurent)
                    vertexList.append(current)
                    path = []
                    y=End
                    
                    while y != -1:
                        path.append(y)
                        y=n[y]
                        path.reverse()
                        return path
                    print("So, the path is :",bfs(graph,0,5))
