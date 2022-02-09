graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : ['H', 'I'],
    'E' : ['J'],
    'F' : ["K"],
    'G' : [],
    'H' : [],
    'I' : [],
    'J' : [],
    'K' : []
}

def dls(start, goal, path, level, maxD):
    print('\nCurrent level-->', level)
    print('Goal node testing for', start)
    path.append(start)
    if start == goal:
        print("Goal test successfull")
        return path
    print('Goal node testing failed')
    if level==maxD:
        return False
    print('\nExpanding the current node', start)
    for child in graph[start]:
        if dls(child, goal, path, level+1, maxD):
            return path
        path.pop()
    return False

start = 'A'
goal = input("Enter the goal node:-'")
maxD = int(input("Enter the maximum depth limit:-"))
print()
path = list()
res = dls(start, goal, path, 0, maxD)
if(res):
    print("Path to goal node available")
    print("Path", path)
else:
    print("No path available for the goal node in given depth limit")