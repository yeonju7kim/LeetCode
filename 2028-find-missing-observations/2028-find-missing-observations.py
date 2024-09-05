class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        total_length = len(rolls) + n
        total_sum = mean * total_length
        rolls_sum = sum(rolls)
        remainder_sum = total_sum - rolls_sum
        average_remainder = float(remainder_sum) / float(n)
        answer = []
        if average_remainder > 6:
            pass
        elif average_remainder < 1:
            pass
        else:
            for i in range(n):
                if float(remainder_sum) % float(n - i) == 0:
                    answer = answer + [int(float(remainder_sum) / float(n - i))] * (n - i)
                    break
                else:
                    if remainder_sum - int(math.ceil(average_remainder)) == 0:
                        new_item = int(math.ceil(average_remainder)) - 1
                        answer.append(new_item)
                        remainder_sum = remainder_sum - new_item
                    else:
                        new_item = int(math.ceil(average_remainder))
                        answer.append(new_item)
                        remainder_sum = remainder_sum - new_item
        return answer