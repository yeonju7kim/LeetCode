class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        result = [0] * n

        # First pass: calculate left-to-right cumulative cost
        count = 0
        moves = 0
        for i in range(n):
            result[i] += moves
            count += int(boxes[i])
            moves += count

        # Second pass: calculate right-to-left cumulative cost
        count = 0
        moves = 0
        for i in range(n - 1, -1, -1):
            result[i] += moves
            count += int(boxes[i])
            moves += count

        return result
