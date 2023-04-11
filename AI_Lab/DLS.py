def dls(graph, cost, node, goal, depth, max_depth):
    if node == goal:
        print("Solution found")
        print("Solution path =", path)
        pathcost = calculate_path_cost(path, cost)
        print("Path cost =", pathcost)
        return True

    if depth == max_depth:
        return False

    if node not in expanded:
        expanded.append(node)

    if depth == 0:
        print("Current node:", node)
        print("Expanded nodes:", expanded)

    if depth > 0:
        print("Current node:", node)

    neighbours = graph[node]
    for n in neighbours:
        if n not in expanded:
            path.append(n)
            if dls(graph, cost, n, goal, depth+1, max_depth):
                return True
            path.pop()

    return False

def calculate_path_cost(path, cost):
    pathcost = 0
    for i in range(1, len(path)):
        edge = path[i-1] + path[i]
        step_cost = cost[edge]
        pathcost += step_cost
    return pathcost

# Graph representation
graph = {'a': ['b', 'c'], 'b': ['c', 'd', 'e'], 'c': ['d', 'e'], 'd': ['g'], 'e': ['d', 'g']}
cost = {'ab': 5, 'ac': 2, 'bc': 6, 'bd': 2, 'be': 8, 'cd': 7, 'ce': 6, 'dg': 6, 'ed': 5, 'eg': 4}

# Start and goal nodes
start = 'a'
goal = 'g'

# Depth-Limited Search (DLS) with maximum depth of 3
expanded = []
path = [start]
max_depth = 3
dls(graph, cost, start, goal, 0, max_depth)
