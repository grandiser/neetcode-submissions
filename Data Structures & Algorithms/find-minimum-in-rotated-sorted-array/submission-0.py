class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 3 4 5 6 1 2
        # if nums[0] < nums[-1]: return nums[0]
        # 
        # 6 1 2 3 4 5
        # l         r
        # l r
        #. lr

        l, r = 0, len(nums) - 1

        while l < r:
            pivot = (l+r)//2

            if nums[pivot] > nums[-1]:
                l = pivot + 1
            elif nums[pivot] < nums[-1]:
                r = pivot
        
        return nums[l]