# https://leetcode.com/problems/find-a-peak-element-ii/
"""
思路
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.


- 每一row找到 row的max value的index, let's say i
- 那么 在下面的情况

row-1 [      i        ]
row   [      i,       ]
row+1 [      i        ]


mat[row-1][i] 
mat[row][i]
mat[row+1][i]

如果 mat[row+1][i] > mat[row][i]
那么 regional max有可能在 row+1中 因为 i_col_max for row+1 一定比row 那个位置要大
"""


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def _get_col_max_fromrow_index(row):
            max = row[0]
            max_col_index = 0
            for c, value in enumerate(row, 0):
                if value > max:
                    max = value
                    max_col_index = c
            return max_col_index

        row_size = len(mat)
        col_size = len(mat[0])

        start = 0
        end = row_size - 1
        while start < end:
            mid = start + (end - start) // 2
            mid_col_max = _get_col_max_fromrow_index(mat[mid])
            if mid > 0 and mat[mid - 1][mid_col_max] > mat[mid][mid_col_max]:
                end = mid - 1
            elif (
                mid + 1 < row_size and mat[mid + 1][mid_col_max] > mat[mid][mid_col_max]
            ):
                start = mid + 1
            else:
                return [mid, mid_col_max]
        # singular row case
        return [start, _get_col_max_fromrow_index(mat[start])]
