class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        # 3 4 5 6 7
        # 4
        row_idx = -1

        l, r = 0, rows - 1

        while l <= r:
            mid = (l+r)//2
            small, big = matrix[mid][0], matrix[mid][cols-1]

            if target < small:
                r = mid - 1
            if target > big:
                l = mid + 1
            if small <= target <= big:
                row_idx = mid
                break
        
        if row_idx == -1:
            return False
        
        l, r = 0, cols - 1

        while l <= r:
            mid = (l+r)//2

            if target < matrix[row_idx][mid]:
                r = mid - 1
            elif target > matrix[row_idx][mid]:
                l = mid + 1
            elif target == matrix[row_idx][mid]:
                return True
        
        return False


