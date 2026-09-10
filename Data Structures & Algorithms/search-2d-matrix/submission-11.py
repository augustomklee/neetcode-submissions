class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # First search
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            m = (top + bot) // 2

            # Target to the left
            if matrix[m][0] > target:
                bot = m - 1
            # Target to the right
            elif matrix[m][-1] < target:
                top = m + 1
            else:
                break
        
        if not top <= bot:
            return False
        row = (top + bot) // 2
        l, r = 0, len(matrix[0]) - 1
        
        while l <= r:
            m = (r + l) // 2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        return False
