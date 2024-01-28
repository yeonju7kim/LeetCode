class Solution:
    def jump(self, nums: List[int]) -> int:
        num_length = len(nums)
        arr = [1000000] * num_length
        arr[0] = 0
        for i in range(num_length):
            cur_count = arr[i]
            for j in range(nums[i]):
                next_step = i + j + 1
                if next_step < num_length:
                    if cur_count + 1 < arr[next_step]:
                        arr[next_step] = cur_count + 1
                else:
                    break
        return arr[-1]