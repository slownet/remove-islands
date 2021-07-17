"""
The task was stolen from the video down bellow:
https://www.youtube.com/watch?v=4tYoVx0QoN0

Given the matrix with zeros and ones the goal is to remove islands.
An island is a group of ones which is not connected to the matrix edge.

"""
import collections
from pprint import pprint

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

IS_NODE_CONNECTED: dict = {}


def get_neighbours(i, j, matrix) -> [(int, int)]:
    matrix_height = len(matrix)
    matrix_width = len(matrix[0])

    if i < 0 or i >= matrix_height:
        raise ValueError('Invalid i-th coordinate!')

    if j < 0 or j >= matrix_width:
        raise ValueError('Invalid j-th coordinate!')

    pre_neighbours = [
        (i + 1, j),  # down
        (i, j + 1),  # right
        (i - 1, j),  # up
        (i, j - 1),  # left
    ]

    neighbours = []

    for i, j in pre_neighbours:
        if is_valid_cell(i, j, matrix):
            neighbours.append((i, j))

    return neighbours


def is_valid_cell(i, j, matrix) -> bool:
    matrix_height = len(matrix)
    matrix_width = len(matrix[0])

    if 0 <= i < matrix_height and 0 <= j < matrix_width:
        return True

    return False


def is_border_node(i, j, matrix) -> bool:
    matrix_height = len(matrix)
    matrix_width = len(matrix[0])

    if not is_valid_cell(i, j, matrix):
        return False

    if i == 0 or i == matrix_height - 1:
        return True

    if j == 0 or j == matrix_width - 1:
        return True

    return False


def is_connected_with_edge(i, j, matrix) -> bool:
    queue = collections.deque([(i, j)])
    visited = set()

    while queue:
        node = queue.popleft()

        i, j = node

        if matrix[i][j] == 0:
            continue

        if is_border_node(i, j, matrix):
            return True

        for neighbour in get_neighbours(node[0], node[1], matrix):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


def get_cells_to_remove(matrix):
    matrix_height = len(matrix)
    matrix_width = len(matrix[0])

    to_remove = [[0 for col in range(matrix_width)] for row in range(matrix_height)]

    for i in range(matrix_height):
        for j in range(matrix_width):
            if matrix[i][j] == 0:
                continue

            if not is_border_node(i, j, matrix) and not is_connected_with_edge(i, j, matrix):
                to_remove[i][j] = 1

    return to_remove


def remove_cells(original_matrix, mask):
    matrix_height = len(original_matrix)
    matrix_width = len(original_matrix[0])

    for i in range(matrix_height):
        for j in range(matrix_width):
            if original_matrix[i][j] == 0:
                continue

            if mask[i][j]:
                original_matrix[i][j] = 0


if __name__ == '__main__':
    cells_to_remove = get_cells_to_remove(sample_matrix)
    pprint(cells_to_remove)

    print()

    remove_cells(sample_matrix, cells_to_remove)
    pprint(sample_matrix)

