class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_nums = sorted(list(set(nums)))
        for i in range(len(new_nums)):
            nums[i] = new_nums[i]
        return len(new_nums)
    