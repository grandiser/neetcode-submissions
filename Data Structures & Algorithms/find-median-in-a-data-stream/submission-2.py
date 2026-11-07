class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        l,r = 0, len(self.nums)-1
        while l <= r:
            mid = (l+r)//2
            if num == self.nums[mid]:
                self.nums.insert(mid, num)
                return
            elif num > self.nums[mid]:
                l = mid+1
            elif num < self.nums[mid]:
                r = mid - 1
        self.nums.insert(l, num)
        

    def findMedian(self) -> float:
        # 1 2 3 4 5 6 7 
        # 
        mid = (len(self.nums)-1) // 2
        if len(self.nums) % 2 == 0:
            return (self.nums[mid] + self.nums[mid+1]) / 2
        else:
            return self.nums[mid]
        
        