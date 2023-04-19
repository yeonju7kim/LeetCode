class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        cnt = [0] * len(nums)
        for i, n in enumerate(nums):
            if i == 0:
                continue
            cnt[i] = nums[i] - nums[i - 1] - 1 + cnt[i - 1]
            if cnt[i] >= k:
                return nums[i - 1] + k - cnt[i - 1]
        return nums[len(nums) - 1] + k - cnt[len(nums) - 1]