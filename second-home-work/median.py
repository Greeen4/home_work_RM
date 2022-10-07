class MedianFinder():
    def __init__(self):
        self.lst = []
        self.len_lst = 0


    def addNum(self, number):
        self.lst.append(number) 
        self.len_lst += 1


    def findMedian(self):
        if not self.len_lst: return 0

        if self.len_lst % 2:
            return self.lst[self.len_lst // 2]

        return (self.lst[self.len_lst // 2] + self.lst[self.len_lst // 2 - 1]) / 2

