CANNOT = -10000
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        arr = []
        for i in range(amount):
            min_candidate = []
            for c in coins:
                if c < i + 1 and i - c >= 0:
                    if arr[i-c] != CANNOT:
                        min_candidate.append(arr[i - c] + 1)
                elif c == i + 1:
                    min_candidate.append(1)
                else:
                    break
            if len(min_candidate) == 0:
                arr.append(CANNOT)
            else:
                arr.append(min(min_candidate))
        if len(arr) == 0:
            return 0
        if arr[-1] == CANNOT:
            return -1
        return arr[-1]