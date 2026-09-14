class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Find all current zeroes
        zeroesSet = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zeroesSet.add((i,j))
        
        for t in zeroesSet:
            i, j = t
            # row
            for m in range(len(matrix[i])):
               matrix[i][m] = 0
            # col
            for n in range(len(matrix)):
               matrix[n][j] = 0