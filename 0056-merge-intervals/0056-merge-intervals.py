class Solution(object):
    def isOverlap(self, int1, int2):
        if (int1[1] < int2[0] and int1[1] < int2[1]) or (int2[1] < int1[0] and int2[1] < int1[1]):
            return False
        return True
    
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals)
        cur = intervals[0]
        answer = []
        for interval in intervals[1:]:
            if self.isOverlap(cur, interval):
                cur[0] = min(cur[0], interval[0])
                cur[1] = max(cur[1], interval[1])
            else:
                answer.append(cur)
                cur = interval
        if len(answer) ==0 or cur != answer[-1]:
            answer.append(cur)
        return answer
                
        