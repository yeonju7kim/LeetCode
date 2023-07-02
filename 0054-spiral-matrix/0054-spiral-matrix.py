class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def isValid(pos: list):
            if pos[0] < 0:
                return False
            if pos[1] < 0:
                return False
            if pos[0] >= len(matrix):
                return False
            if pos[1] >= len(matrix[0]):
                return False
            return True
        
        ans = []
        visit = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        # visit = [False] *  len(matrix[0])
        pos = [0,0]
        cur_state = 0
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        while(True):
            visit[pos[0]][pos[1]] = True
            ans.append(matrix[pos[0]][pos[1]])
            next_pos = [pos[0] + direction[cur_state][0], pos[1] + direction[cur_state][1]]
            if isValid(next_pos) and visit[next_pos[0]][next_pos[1]] == False:
                pos = next_pos
            else:
                cur_state = (cur_state + 1) % 4
                next_pos = [pos[0] + direction[cur_state][0], pos[1] + direction[cur_state][1]]
                if isValid(next_pos) and visit[next_pos[0]][next_pos[1]] == False:
                    pos = next_pos
                else:
                    break
        return ans
                