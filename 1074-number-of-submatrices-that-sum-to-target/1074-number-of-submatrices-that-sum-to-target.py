class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row = len(matrix) + 1
        col = len(matrix[0]) + 1
        count_matrix = [[0]*col for _ in range(row)]
        for r in range(1, row):
            for c in range(1, col):
                count_matrix[r][c] = count_matrix[r - 1][c]+ count_matrix[r][c - 1] - count_matrix[r - 1][c - 1] + matrix[r - 1][c - 1]

        answer = 0

        for r1 in range(1, row):
            for c1 in range(1, col):
                for r2 in range(r1, row):
                    for c2 in range(c1, col):
                        sub_sum = count_matrix[r2][c2] - count_matrix[r1 - 1][c2] - count_matrix[r2][c1 - 1] + count_matrix[r1 - 1][c1 - 1]
                        if sub_sum == target:
                            answer = answer + 1
        
        return answer
        
        