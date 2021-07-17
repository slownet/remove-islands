import unittest
from unittest import TestCase

from main import get_neighbours, is_border_node, get_cells_to_remove, remove_cells

TEST_MATRIX = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
]


class TestIsBorderLine(TestCase):
    def test_corner_cell(self):
        self.assertTrue(is_border_node(0, 0, TEST_MATRIX))
        self.assertTrue(is_border_node(5, 5, TEST_MATRIX))
        self.assertTrue(is_border_node(5, 0, TEST_MATRIX))
        self.assertTrue(is_border_node(0, 5, TEST_MATRIX))

        self.assertFalse(is_border_node(1, 1, TEST_MATRIX))
        self.assertFalse(is_border_node(3, 2, TEST_MATRIX))


class TestGetNeighbours(TestCase):

    def test_center_cell(self):
        res = get_neighbours(1, 1, TEST_MATRIX)
        self.assertEqual(set(res), {(2, 1), (1, 2), (0, 1), (1, 0)})

        res = get_neighbours(3, 3, TEST_MATRIX)
        self.assertEqual(set(res), {(2, 3), (4, 3), (3, 2), (3, 4)})

    def test_border_cells(self):
        matrix_height = len(TEST_MATRIX)
        matrix_width = len(TEST_MATRIX[0])

        res = get_neighbours(0, 0, TEST_MATRIX)
        self.assertEqual(set(res), {(0, 1), (1, 0)}, f'There is a problem with i=0, j=0')

        res = get_neighbours(matrix_height - 1, 0, TEST_MATRIX)
        self.assertEqual(set(res), {(4, 0), (5, 1)}, f'There is a problem with i={matrix_height - 1}, j=0')

        res = get_neighbours(0, matrix_width - 1, TEST_MATRIX)
        self.assertEqual(set(res), {(0, 4), (1, 5)}, f'There is a problem with i=0, j={matrix_width - 1}')

        res = get_neighbours(matrix_height - 1, matrix_width - 1, TEST_MATRIX)
        self.assertEqual(set(res), {(5, 4), (4, 5)},
                         f'There is a problem with i={matrix_height - 1}, j={matrix_width - 1}')

    def test_invalid_coordinate(self):
        with self.assertRaises(ValueError):
            get_neighbours(len(TEST_MATRIX), 2, TEST_MATRIX)
            get_neighbours(-1, 2, TEST_MATRIX)
            get_neighbours(2, len(TEST_MATRIX[0]), TEST_MATRIX)
            get_neighbours(2, -1, TEST_MATRIX)
            get_neighbours(-5, -5, TEST_MATRIX)
            get_neighbours(len(TEST_MATRIX) + 100, len(TEST_MATRIX[0]) + 100, TEST_MATRIX)


class TestGetCellsToRemove(TestCase):
    def test_sample(self):
        expected = [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]

        actual = get_cells_to_remove(TEST_MATRIX)

        self.assertEqual(actual, expected)


class TestRemoveIslands(TestCase):
    def test_sample(self):
        matrix_to_modify = [
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [1, 0, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 1],
        ]

        expected_result = [
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1],
        ]

        mask = get_cells_to_remove(matrix_to_modify)

        remove_cells(matrix_to_modify, mask)

        self.assertEqual(matrix_to_modify, expected_result)

    def test_no_borders(self):
        matrix_to_modify = [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0],
        ]

        expected_result = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]

        mask = get_cells_to_remove(matrix_to_modify)

        self.assertEqual(mask, matrix_to_modify)
        remove_cells(matrix_to_modify, mask)

        self.assertEqual(matrix_to_modify, expected_result)

    def test_nothing_to_remove(self):
        matrix_to_modify = [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 0],
        ]

        without_changes = [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 0],
        ]

        self.assertEqual(matrix_to_modify, without_changes)

        mask = get_cells_to_remove(matrix_to_modify)
        remove_cells(matrix_to_modify, mask)

        self.assertEqual(matrix_to_modify, without_changes)


if __name__ == '__main__':
    unittest.main()
