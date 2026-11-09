class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counts = defaultdict(int)
        best = 0

        for r in range(len(s)):
            counts[s[r]] += 1

            while max(counts.values()) < (r-l+1) - k:
                counts[s[l]] -= 1
                l += 1
            
            best = max(best, r-l+1)
        
        return best
            
