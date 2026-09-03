class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        the_row = []
        for row in matrix:
            if target <= row[-1]:
                the_row = row
                break
        if len(the_row) > 0:
            for num in row:
                if num == target:
                    return True
        return False