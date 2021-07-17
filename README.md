# Island remover

My solution for the problem from this video: https://www.youtube.com/watch?v=4tYoVx0QoN0

Given the matrix with zeros and ones the goal is to remove "islands".
An island is a group of ones which is not connected to the matrix edge.

    sample_matrix = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1],
    ]
    
    sample_output = [
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1],
    ]
    
    removed_cells = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    
    
The solution is based on Breadth-first search in 
order to find a path to the edge. The script still 
lacks caching, which is very easy to add (see 
prepared IS_NODE_CONNECTED dict which might store 
such information per every cell).