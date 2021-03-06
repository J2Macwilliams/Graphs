"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}
        

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Vertex does not exist.')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # instantiate an empty Queue and add starting vertex to it
        q = Queue()
        q.enqueue(starting_vertex)

        # create a set to store vertices visited
        visited = set()

        # create base case loop to end when all items have left the queue
        while q.size() > 0:
            # dequeue the first item
            v = q.dequeue()

            # check if v has been visited?
            if v not in visited:
                # add vto visited
                visited.add(v)
                print(v)

                # acquire all the neighbors of v and add to queue
                for next_vertex in self.get_neighbors(v):
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # instantiate an empty Stack and add starting vertex to it
        s = Stack()
        s.push(starting_vertex)

        # create a set to store vertices visited
        visited = set()

        # create base case loop to end when all items have left the queue
        while s.size() > 0:
            # pop the first item
            v = s.pop()

            # check if v has been visited?
            if v not in visited:
                # add vto visited
                visited.add(v)
                print(v)

                # acquire all the neighbors of v and push them to the stack
                for next_vertex in self.get_neighbors(v):
                    s.push(next_vertex)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print(starting_vertex)
        for new_vect in self.get_neighbors(starting_vertex):
            if new_vect < starting_vertex:
                return
            self.dft_recursive(new_vect)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue and enqueue PATH To the Starting Vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first PATH
            path = q.dequeue()
            # grab the last vertex from the Path
            last = path[-1]
            
            # check if the vertex has not been visited
            if last not in visited:
                # is this vertex the target?
                if last is destination_vertex:
                    # return the path
                    return path
                    
                # mark it as visited
                visited.add(last)
                # then add A Path to its neighbors to the back of the queue
                for next_vertex in self.get_neighbors(last):
                    
                    # make a copy of the path
                    path_copy = list(path)
                    # append the neighbor to the back of the path
                    path_copy.append(next_vertex)
                    # enqueue out new path
                    q.enqueue(path_copy)

        
        # return none
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty stack and push PATH To the Starting Vertex ID
        s = Stack()
        s.push([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while the stack is not empty
        while s.size() > 0:
            # pop the first PATH
            path = s.pop()
            # grab the last vertex from the Path
            last = path[-1]
            
            # check if the vertex has not been visited
            if last not in visited:
                # is this vertex the target?
                if last is destination_vertex:
                    # return the path
                    return path
                    
                # mark it as visited
                visited.add(last)
                # then add A Path to its neighbors to the back of the queue
                for next_vertex in self.get_neighbors(last):
                    
                    # make a copy of the path
                    path_copy = list(path)
                    # append the neighbor to the back of the path
                    path_copy.append(next_vertex)
                    # push out new path
                    s.push(path_copy)

        # return none
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        
        # my_code(it works, but not pretty)
        path += [starting_vertex]
        # create the base case
        if starting_vertex is destination_vertex:
            return path
        for next_vertex in self.vertices[starting_vertex]:
            if next_vertex not in path:
                path = self.dfs_recursive(next_vertex, destination_vertex, path)
            if next_vertex is destination_vertex:
                return path
        if destination_vertex not in path:
            path.pop()
        return path    
            
        


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
