def initial_graph():
    return {

        'A': {'B': 3, 'S': 7, 'D': 4},
        'B': {'A': 3, 'S': 2, 'C': 12,'H': 1},
        'C': {'S': 3, 'B': 12, 'L': 2},
        'D': {'A': 4, 'F': 5, 'H': 4},
        'E': {'G': 2, 'K': 5},
        'F': {'H': 3, 'D': 5, },
        'G': {'H': 2, 'I': 10, 'E': 2},
        'H': {'D': 4, 'B': 1, 'F': 3, 'G': 2},
        'I': {'G': 10, 'J': 6, 'L': 4, 'K': 4},
        'J': {'L': 4, 'I': 6, 'K': 4},
        'K': {'I': 4, 'J': 4, 'E': 5},
        'L': {'C': 2, 'I': 4, 'J': 4},
        'S': {'A': 7, 'B': 2, 'C': 3}

    }


print(initial_graph())

initial = 'A'
path = {}
adj_node = {}
queue = []
graph = initial_graph()
for node in graph:
    path[node] = float("inf")
    adj_node[node] = None
    queue.append(node)

path[initial] = 0
while queue:
    # find min distance which wasn't marked as current
    key_min = queue[0]
    min_val = path[key_min]
    for n in range(1, len(queue)):
        if path[queue[n]] < min_val:
            key_min = queue[n]
            min_val = path[key_min]
    cur = key_min
    queue.remove(cur)
    print(cur)

    for i in graph[cur]:
        alternate = graph[cur][i] + path[cur]
        if path[i] > alternate:
            path[i] = alternate
            adj_node[i] = cur

x = 'E'
print('The path between A to E')
print(x, end='<-')
while True:
    x = adj_node[x]
    if x is None:
        print("")
        break
    print(x, end='<-')