class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        hash_chars = defaultdict(int)
        for c in chars:
            hash_chars[c] += 1
        for word in words:
            checked = False
            hash_word = defaultdict(int)
            for w in word:
                hash_word[w] += 1
            for k, v in hash_word.items():
                if v > hash_chars[k]:
                    checked = True
                    break
            if checked == False:
                ans += len(word)
        return ans