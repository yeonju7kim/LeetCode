class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        trie = []
        for num in arr1:
            cur_trie = trie
            num_str = str(num)
            for c in num_str:
                done = False
                for k in cur_trie:
                    if k.keys()[0] == c:
                        cur_trie = k[c]
                        done = True
                        break
                if done == False:
                    new_node = {c:[]}
                    cur_trie.append(new_node)
                    cur_trie = cur_trie[-1][c]
        max_length = -1
        
        for num in arr2:
            cur_trie = trie
            num_str = str(num)
            for i, c in enumerate(num_str):
                done = False
                for k in cur_trie:
                    if k.keys()[0] == c:
                        cur_trie = k[c]
                        done = True
                        break
                if done == False:
                    if i > max_length:
                        max_length = i
                    break
                if i + 1 > max_length:
                    max_length = i + 1
        return max_length
