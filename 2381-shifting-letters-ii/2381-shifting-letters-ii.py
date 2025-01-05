class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        shift_array = [0] * (n + 1)  # 누적 합 계산을 위한 배열
        
        # 누적 합을 사용해 shifts 적용
        for start, end, direction in shifts:
            shift_array[start] += 1 if direction == 1 else -1
            shift_array[end + 1] -= 1 if direction == 1 else -1
        
        # shift_array의 누적 합 계산
        for i in range(1, n):
            shift_array[i] += shift_array[i - 1]
        
        # 문자열 변환
        result = []
        for i in range(n):
            new_char = chr((ord(s[i]) - ord('a') + shift_array[i]) % 26 + ord('a'))
            result.append(new_char)
        
        return ''.join(result)
