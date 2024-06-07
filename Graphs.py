# Adjacency Matrix Representation of a Graph
n, m = map(int, input().split()) # n - number of nodes, m - number of edges

# Initialize an n+1 x n+1 matrix with zeros
adj_matrix = [[0] * (n + 1) for _ in range(n + 1)]

# Read edges and populate the adjacency matrix
for _ in range(m):
    u, v = map(int, input().split())
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1

# Print the adjacency matrix
print("Adjacency Matrix Representation:")
for row in adj_matrix:
    print(row)

# Adjacency List Representation of a Graph
n, m = map(int, input().split()) 
adj_list = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)
print("\nAdjacency List Representation:")
for neighbors in adj_list:
    print(neighbors)

# Breadth-First Search Algorithm
def initiateBFS(node, visited, adj, result):
    queue = [node]
    visited[node] = True
    while queue:
        currnode = queue.pop(0)
        result.append(currnode)
        for neighbor in adj[currnode]:
            if visited[neighbor] == False:
                visited[neighbor] = True
                queue.append(neighbor)
    
def printBFS(adj, n):
    visited = [False] * n
    result = []
    for node in range(n):
        if visited[node] == False:
            initiateBFS(node, visited, adj, result)
    print("\nBFS traversal is", result)

printBFS(adj_list, n + 1)

# Depth First Search Algorithm
def initiateDFS(node, visited, adj, result):
    result.append(node)
    visited[node] = True
    for neighbor in adj[node]:
        if visited[neighbor] == False:
            initiateDFS(neighbor, visited, adj, result)
 
def printDFS(adj, n):
    visited = [False] * n
    result = []
    for node in range(n):
        if visited[node] == False:
            initiateDFS(node, visited, adj, result)
    print("DFS Traversal is", result)

printDFS(adj_list, n + 1)