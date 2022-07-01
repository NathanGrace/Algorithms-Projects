# Nathan Grace
# Reference: Dfs_ code discussed in class

# An iterative DFS implementation 
# 
# -GRAPH: a dictionary of vertex and adjancent list
# -START: starting vertex for traversal
# -VISITED: a set of visited vertices 
#
def _dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        #print('The stack is:', stack)
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                print(path + [next])
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def bfs(graph, start):
    visited, queue = set(), [start]
    p =[]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            p.append(vertex)
            queue.extend(graph[vertex] - visited)
    return p

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                print(path + [next])
                yield path + [next]               
            else:
                queue.append((next, path + [next]))
                
def main():
    # Sample graphs
    graph = {'A': set(['B', 'F', 'E']),
             'B': set(['A', 'F', 'C']),
             'C': set(['B', 'G', 'D']),
             'D': set(['C', 'G']),
             'E': set(['A', 'F', 'I']),
             'F': set(['A', 'E', 'B']),
             'G': set(['C', 'D', 'J']),
             'H': set(['K', 'L']),
             'I': set(['E', 'F', 'J', 'M']),
             'J': set(['I', 'G']),
             'K': set(['H', 'L', 'O']),
             'L': set(['H', 'K', 'P']),
             'M': set(['I', 'N']),
             'N': set(['M']),
             'O': set(['K']),
             'P': set(['L'])}
    
    print('\n')
    
    print('DFS starting from "A":')
    v = _dfs(graph, 'A')
    print(v)
    
    print('\n')
    
    print('DFS starting from "H":')
    v2 = _dfs(graph, 'H')
    print(v2)
    
    print('\n')
    
    print('DFS Paths from A to D:')
    list(dfs_paths(graph, 'A', 'D'))
    
    print('\n')
    
    print('BFS starting from "A:"')
    v3 = bfs(graph, 'A')
    print(v3)
    
    print('\n')
    
    print('BFS starting from "H":')
    v4 = bfs(graph, 'H')
    print(v4)
    
    print('\n')
    print('BFS Paths from A to D:')
    list(bfs_paths(graph, 'A', 'D'))
    

if __name__ == '__main__':
    main()
