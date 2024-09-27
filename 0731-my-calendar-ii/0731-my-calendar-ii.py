class MyCalendarTwo(object):

    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        overlap = []
        for (s, e) in self.calendar:
            if max(s, start) < min(e, end):
                overlap.append([max(s, start), min(e, end)])
        if len(overlap) == 0:
            self.calendar.append([start, end])
            return True
        else:
            for i in range(len(overlap)):
                for j in range(len(overlap)):      
                    if i == j:
                        continue
                    if max(overlap[i][0], overlap[j][0]) < min(overlap[i][1], overlap[j][1]):
                            return False
        self.calendar.append([start, end])
        return True