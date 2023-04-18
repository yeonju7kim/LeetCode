class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0 
        r = len(nums) - 1
        lowerbound = 0
        upperbound = 0
        while(l <= r):
            m = (int)((l + r) / 2)
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            elif nums[m] == target:
                if m > 0 and nums[m - 1] != target:
                    lowerbound = m
                    break
                elif m == 0:
                    lowerbound = 0
                    break
                else:
                    r = m - 1

        l = lowerbound 
        r = len(nums) - 1
        while(l <= r):
            m = (int)((l + r) / 2)
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            elif nums[m] == target:
                if m + 1 < len(nums) and nums[m + 1] != target:
                    upperbound = m
                    break
                elif m == len(nums) - 1:
                    upperbound = m
                    break
                else:
                    l = m + 1
        if len(nums) == 0 or (lowerbound == 0 and upperbound == 0 and nums[0] != target):
            return [-1, -1]
        return [lowerbound, upperbound]            