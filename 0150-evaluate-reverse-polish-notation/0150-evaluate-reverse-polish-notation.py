class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        
        s = []
        
        for t in tokens:
            if t not in ["*", "/", "+", "-"]:
                s.append(t)
            else:
                top_num = int(s.pop())
                second_num = int(s.pop())
                if t == "*":
                    result = second_num * top_num
                elif t == "/":
                    result = second_num / top_num
                elif t == "+":
                    result = second_num + top_num
                elif t == "-":
                    result = second_num - top_num
                s.append(result)
        
        return int(s[-1])