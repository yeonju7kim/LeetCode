class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        answer = 0
        summ = 0
        for n in nums:
            summ += n
            if summ - k in count:
                answer += count[summ - k]
            count[summ] += 1
        return answer