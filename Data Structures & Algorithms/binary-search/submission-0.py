class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = -1
        
        # do work
        l, r = 0, len(nums) - 1

        # -1 0 2 4 6 8
        # 4
        #
        #

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                ans = mid
                break
            if nums[mid] > target:
                r = mid - 1
            
            if nums[mid] < target:
                l = mid + 1

        return ans