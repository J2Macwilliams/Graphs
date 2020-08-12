"""
## Understand
DFS 
iterative
make a path
returns the earliest known Ancestor(last item on the returned path)

"""
from util import Stack
from graph import Graph
 
def get_neighbors(ancestors, vertex):
    # set up a graph
    lineage = Graph()
    # loop thru ancestors to add vertices
    for pair in ancestors:
        lineage.add_vertex(pair[0])
    # loop thru ancestors to add edges
    for pair in ancestors:
        lineage.add_edge(pair)

def earliest_ancestor(ancestors, starting_node):
    # create a graph
    lineage = Graph()
    # loop thru ancestors to create vertices
    for pair in ancestors:
        # add vertices to graph
        lineage.add_vertex(pair[0])
        lineage.add_vertex(pair[1])
    # loop thru to create edges
    for pair in ancestors:
        lineage.add_edge(pair[1],pair[0])
    # create list to hold paths
    paths = []
    # create an empty stack
    s = Stack()
    # push starting path onto Stack
    s.push([starting_node])
    # make a set of visited vetices
    visited = set()
    
    # create a loop to search for the ancestor
    while s.size() > 0:
        # pop off the top item on the stack
        path = s.pop()
        # grab the last item from path
        v = path[-1]
        # check to see if v has ancestors
            # if not return v
        # check if it has been visited
        if v not in visited:
            # if not add to visited
            visited.add(v)
            paths.append(path)
        # print('v',v)
        # print('lineage',lineage.get_neighbors(v))
        # find neighbors of the vertex
            for next_v in lineage.get_neighbors(v):
                # make a copy of the path
                path_copy = list(path)
                # append the next_v to the copy
                path_copy.append(next_v)
                paths.append(path_copy)
                # push copy onto Stack
                s.push(path_copy)
    print(paths)
    paths_len = [len(x) for x in paths]
    same = []
    paths_max = max(paths_len)
    # check for if there are no parents         
    if paths_max == 1:
        return -1
    else:
        for p in paths:
            if len(p) == paths_max:
                same.append(p[-1])
        return min(same)


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 1)