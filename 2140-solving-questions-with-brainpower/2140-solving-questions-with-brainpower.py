class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        memo = [q[0] for q in questions]
        l = len(questions)
        for idx in range(l - 2, -1, -1):
            new_idx = questions[idx][1] + idx + 1
            if new_idx < l:
                memo[idx] = memo[new_idx] + memo[idx]
            memo[idx] = max(memo[idx], memo[idx + 1])
        return memo[0]