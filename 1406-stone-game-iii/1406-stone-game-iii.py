class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [[-1 for _ in range(n + 1)] for _ in range(2)]
        def f(p, i):
            if i >= n:
                return 0
            if dp[p][i] != -1:
                return dp[p][i]
            res = -1000000 if p == 0 else 1000000 
            for j in range(3):
                max_index = min(i+j+1, n)
                if p == 0:
                    s = sum(stoneValue[i:max_index])
                    res = max(res, s + f(p^1 , max_index))
                else:
                    res = min(res, f(p^1 , max_index))
            dp[p][i] = res
            return res
        alice = f(0,0)
        bob = sum(stoneValue) - alice
        if bob < alice:
            return "Alice"
        elif bob > alice:
            return "Bob"
        return "Tie"