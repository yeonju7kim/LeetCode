class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visit = defaultdict(int)
        for n in nums:
            if n in visit:
                return n
            visit[n] = 0
        return 0