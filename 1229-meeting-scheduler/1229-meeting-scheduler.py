class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        pt1 = pt2 = 0
        
        while pt1 < len(slots1) and pt2 < len(slots2):
            left = max(slots1[pt1][0], slots2[pt2][0])
            right = min(slots1[pt1][1], slots2[pt2][1])
            if right - left >= duration:
                return [left, left + duration]
            if slots1[pt1][1] < slots2[pt2][1]:
                pt1 = pt1 + 1
            else:
                pt2 = pt2 + 1
        return []