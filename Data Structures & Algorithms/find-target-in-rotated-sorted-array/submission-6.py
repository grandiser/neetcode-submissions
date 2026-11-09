class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 3 4 5 6 1 2
        # 
        # 6 1 2 3 4 5

        # 1 2 3 4 5
        #

        def findmin(nums: List[int]) -> int:
            l, r = 0, len(nums) - 1

            while l < r:
                pivot = (l+r) // 2

                if nums[pivot] < nums[-1]:
                    r = pivot
                
                if nums[pivot] > nums[-1]:
                    l = pivot + 1
            
            return r
        
        min_index = findmin(nums)
        print(min_index)

        if min_index == 0:
            l = 0
            r = len(nums) - 1
        elif target > nums[-1]:
            l = 0
            r = min_index - 1
        else:
            l = min_index
            r = len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid

        return -1
            
