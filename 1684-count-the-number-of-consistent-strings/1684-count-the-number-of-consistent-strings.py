class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        ans = 0
        for word in words:
            set_word = set(list([w for w in word]))
            for w in set_word:
                not_allowed = False
                if w not in allowed:
                    not_allowed = True
                    break
            if not_allowed == False:
                ans = ans + 1
        return ans