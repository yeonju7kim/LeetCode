class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        start_binary = "{0:b}".format(start)
        goal_binary = "{0:b}".format(goal)
        max_length = len(start_binary) if len(start_binary) > len(goal_binary) else len(goal_binary)
        start_binary = ''.join(['0'] * (max_length - len(start_binary))) + start_binary
        goal_binary = ''.join(['0'] * (max_length - len(goal_binary))) + goal_binary 
        answer = 0
        for i in range(max_length):
            if start_binary[i] != goal_binary[i]:
                answer = answer + 1
        return answer