class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ans = ""
        i = 0
        l = len(s)
        if numRows == 1:
            return s
        while(i < l):
            ans = ans + s[i]
            i = i + 2 * numRows - 2
        for i in range(1, numRows - 1):
            j = i
            while(j < l):
                ans = ans + s[j]
                if j + 2 * (numRows - 1 - i) < l:
                    ans = ans + s[j + 2 * (numRows - 1 - i)]
                j = j + 2 * numRows - 2
        i = numRows - 1
        while(i < l):
            ans = ans + s[i]
            i = i + 2 * numRows - 2
        return ans