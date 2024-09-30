class CustomStack(object):
    max_size = 0
    stack = []

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.max_size = maxSize
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) < self.max_size:
            self.stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return -1
        return self.stack.pop()
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        for i in range(min(k, len(self.stack))):
            self.stack[i] = self.stack[i] + val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)