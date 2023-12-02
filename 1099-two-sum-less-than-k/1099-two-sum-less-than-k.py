class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_value = -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                s = nums[i] + nums[j]
                if s > max_value and s < k:
                    max_value = s
        return max_value