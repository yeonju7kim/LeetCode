class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        box_length = len(boxes)
        left_count = [0] * box_length
        right_count = [0] * box_length 
        left_accum = [0] * box_length
        right_accum = [0] * box_length
        for i in range(1, box_length):
            left_count[i] = left_count[i - 1] + int(boxes[i - 1])
            right_count[box_length - i - 1] = right_count[box_length - i] + int(boxes[box_length - i]) 
            left_accum[i] = left_count[i] + left_accum[i - 1]
            right_accum[box_length - i - 1] = right_count[box_length - i - 1] + right_accum[box_length - i] 
        for i in range(box_length):
            left_accum[i] = left_accum[i] + right_accum[i]
        return left_accum
        