class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        memory = {1:[],2:[],3:[]}
        for i, c in enumerate(colors):
            memory[c].append(i)
        ans = []
        for q in queries:
            i = q[0]
            c = q[1]
            if len(memory[c]) == 0:
                ans.append(-1)
                continue
            l = 0 
            r = len(memory[c]) - 1
            m = 0
            while(l <= r):
                m = (int)((l + r) / 2)
                if memory[c][m] < i:
                    l = m + 1
                elif memory[c][m] > i:
                    r = m - 1
                else:
                    break
            candidate = [abs(memory[c][m] - i)]
            try:
                candidate.append(abs(memory[c][m - 1] - i))
            except:
                pass
            try:
                candidate.append(abs(memory[c][m + 1] - i))
            except:
                pass
            ans.append(min(candidate))
        return ans
            