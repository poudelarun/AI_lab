graph = {'a': ['b', 'c'], 'b': ['c', 'd', 'e'], 'c': ['d', 'e'], 'd': ['g'], 'e': ['d', 'g']}
cost = {'ab': 5, 'ac': 2, 'bc': 6, 'bd': 2, 'be': 8, 'cd': 7, 'ce': 6, 'dg': 6, 'ed': 5, 'eg': 4}
start = 'a'
goal = 'g'

def BFS():
    expanded = []
    fringe = [start]
    pathq = [[start]]

    while fringe:
        node = fringe.pop(0)
        path = pathq.pop(0)

        if node == goal:
            print("Solution found")
            print("Solution path =", path)
            pathcost = calculate_path_cost(path)
            print("Path cost =", pathcost)
            return

        neighbours = graph[node]
        for n in neighbours:
            if n not in expanded:
                fringe.append(n)
                new_path = list(path)
                new_path.append(n)
                pathq.append(new_path)
                expanded.append(n)

def calculate_path_cost(path):
    pathcost = 0
    for i in range(1, len(path)):
        edge = path[i-1] + path[i]
        step_cost = cost[edge]
        pathcost += step_cost
    return pathcost

BFS()
