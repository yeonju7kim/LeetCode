class Solution(object):
    def stoneGameII(self, piles):
        n = len(piles) - 1
        dp = [[[-1] * (len(piles) + 1) for i in range(len(piles) + 1)] for p in range(0, 2)]
        def f(p, i, m):
            if i > n:
                return 0 
            if dp[p][i][m] != -1:
                return dp[p][i][m]
            res = -1 if p == 0 else 10000000
            last_index = min(n, i + 2 * m - 1)
            for elem_num, x in enumerate(range(i, last_index + 1)):
                if p == 0:
                    s = sum(piles[i:x + 1])
                    res = max(res, s + f(p^1, x + 1, max(m, elem_num + 1)))
                else:
                    res = min(res, f(p^1, x + 1, max(m, elem_num + 1)))
            dp[p][i][m] = res
            return res
        return f(0, 0, 1)