class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)
        answer = [[nums[0]]]
        for n in nums[1:]:
            if n - answer[-1][0] <= k:
                if len(answer[-1]) == 3:
                    answer.append([n])
                else:
                    answer[-1].append(n)
            else:
                answer.append([n])
        for ans in answer:
            if len(ans) != 3:
                return []
        return answer