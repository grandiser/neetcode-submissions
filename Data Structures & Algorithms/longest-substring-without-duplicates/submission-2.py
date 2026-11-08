class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        bl = 0
        uniques = set()

        for r in range(len(s)):
            while s[r] in uniques:
                uniques.remove(s[l])
                l += 1

            uniques.add(s[r])
            bl = max(bl, r-l+1)
        
        return bl