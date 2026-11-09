class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1
        
        for k,v in counts.items():
            if v >1 :
                return k