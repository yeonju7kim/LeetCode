from queue import PriorityQueue
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        que = PriorityQueue(maxsize=k)
        sorted_index = [i[0] for i in sorted(enumerate(nums2), key=lambda x:x[1], reverse=True)]
        nums1 = [nums1[i] for i in sorted_index]
        nums2 = [nums2[i] for i in sorted_index]
        for i in range(k):
            que.put(nums1[i])
        summation = sum(que.queue) 
        ans = summation * nums2[k - 1]
        for i in range(k, len(nums1)):
            min_val = que.get()
            score = (summation - min_val + nums1[i]) * nums2[i]
            if min_val > nums1[i]:
                que.put(min_val)
            else:
                que.put(nums1[i])
                summation = summation - min_val + nums1[i]
            
            ans = score if ans < score else ans
        return ans
        