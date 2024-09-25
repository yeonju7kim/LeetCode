class Trie:
    def __init__(self):
        self.cnt = 1
        self.children = [None] * 26
    
    def insert(self, val):
        val_int = ord(val) - ord('a')
        if self.children[val_int] == None:
            self.children[val_int] = Trie()
        else:
            self.children[val_int].cnt += 1
    
    def count_score(self, word):
        if word == '':
            return 0
        w_int = ord(word[0]) - ord('a')
        return self.children[w_int].cnt + self.children[w_int].count_score(word[1:])

class Solution(object):
    def sumPrefixScores(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        trie = Trie()
        for w in words:
            cur_trie = trie
            word_str = str(w)
            for c in word_str:
                cur_trie.insert(c)
                cur_trie = cur_trie.children[ord(c) - ord('a')]
        answer = []
        for w in words:
            answer.append(trie.count_score(w))
        return answer