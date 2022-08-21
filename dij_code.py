
vertex = list(input('Enter the vertices with a space: ').split())
n, vertices, source = len(vertex), dict(), vertex.index(input('Enter the source node: '))    
graph = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]

for i in range(n): vertices[vertex[i]] = i

while True:
    ls = input('Enter the vertices of an edge with weight or "done" to break: ').split()
    if ls != ['done']:
        graph[vertices[ls[0]]][vertices[ls[1]]] = graph[vertices[ls[1]]][vertices[ls[0]]] = int(ls[2])
    else: break

nodes = [[float('inf'), True, ''] for i in range(n)]
nodes[source][0] = 0

def min_distance():
    Min = float('inf')
    for i in range(n):
        if nodes[i][0] < Min and nodes[i][1]: Min, ind = nodes[i][0], i
    return ind

for i in range(n):
    node = min_distance()
    nodes[node][1] = False

    for adj in range(n):
        if graph[node][adj] > 0 and nodes[adj][1] and nodes[adj][0] > nodes[node][0] + graph[node][adj]:
            nodes[adj][0], nodes[adj][2] = nodes[node][0] + graph[node][adj], node

print('\n\n\tNode\tCost\tPath')

for j, i in enumerate(nodes):
    itr, ls = i[2], [j]
    while(itr != ''):
        ls.append(itr)
        itr = nodes[itr][2]
    print('\t', vertex[j], '\t', i[0], end='\t')
    while(len(ls) > 1): print(vertex[ls.pop()], end=' -> ')
    print(vertex[ls.pop()])
