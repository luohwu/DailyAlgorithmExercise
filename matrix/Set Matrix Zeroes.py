from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        """
        Do not return anything, modify matrix in-place instead.
        """
        row_set = set()
        col_set = set()

        m, n = len(matrix), len(matrix[0])

        def set_row_zero(row_idx):
            nonlocal n
            for j in range(n):
                matrix[row_idx][j] = 0

        def set_col_zero(col_idx):
            nonlocal m
            for i in range(m):
                matrix[i][col_idx] = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)
        for item in row_set:
            set_row_zero(item)
        for item in col_set:
            set_col_zero(item)
