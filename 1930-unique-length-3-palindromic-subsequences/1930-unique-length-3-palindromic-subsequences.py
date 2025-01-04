from collections import defaultdict

class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        index_dictionary = defaultdict(list)
        for s_index, s_char in enumerate(s):
            index_dictionary[s_char].append(s_index)
        ans = 0
        for s_char, s_index_list in index_dictionary.items():
            if len(s_index_list) >= 2:
                min_index = min(s_index_list)
                max_index = max(s_index_list)
                char_set = set()
                for i in range(min_index + 1, max_index):
                    char_set.add(s[i])
                ans = ans + len(char_set)
        return ans