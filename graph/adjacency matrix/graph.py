#An Adjacency Matrix A[V][V] is a 2D array of size V × V where V is the number of vertices in a undirected graph.
#If there is an edge between Vx to Vy then the value of A[Vx][Vy] = 1 and A[Vy][Vx]=1, otherwise the value will be zero.
#For a directed graph, if there is an edge between Vx to Vy, then the value of A[Vx][Vy]=1, otherwise the value will be zero.
#------------------------------------------------------------------------------------------------------------------------------------

#creating an undirected graph :

def build_graph(edges):
    matrix = [[0]*len(edges) for i in range(len(edges))]
    
    for edge in edges:
        source = edge[0]
        destination = edge[1]
        
        matrix[source][destination] = 1
        matrix[destination][source] = 1
        
    return matrix

def display_graph(graph):
    for row in range(len(graph)):
        for column in range(len(graph[0])):
            print(graph[row][column], end = " | ")
        print("\n---------------------------")
    
edges = [[0, 1], [0, 2], [0, 4], [1, 2], [1, 3], [2, 3], [3, 4]]
graph = build_graph(edges)
display_graph(graph)

#----------------------------------------------------------------------------

#creating a directed graph :

def build_graph(edges):
    matrix = [[0]*len(edges) for i in range(len(edges))]
    
    for edge in edges:
        source = edge[0]
        destination = edge[1]
        
        matrix[source][destination] = 1
        
    return matrix

def display_graph(graph):
    for row in range(len(graph)):
        for column in range(len(graph[0])):
            print(graph[row][column], end = " | ")
        print("\n---------------------------")
    
edges = [[0, 1], [0, 2], [0, 4], [1, 2], [1, 3], [2, 3], [3, 4]]
graph = build_graph(edges)
display_graph(graph)
