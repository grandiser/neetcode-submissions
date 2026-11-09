class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = [0] * 26
        s2_counts = [0] * 26
        len_s1 = len(s1)

        for l in s1:
            s1_counts[ord(l) - ord('a')] += 1

        l = 0

        for r in range(len(s2)):
        
            if r - l + 1 < len_s1:
                s2_counts[ord(s2[r]) - ord('a')] += 1
                continue

            s2_counts[ord(s2[r]) - ord('a')] += 1

            while r - l + 1 > len_s1:
                s2_counts[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            if s1_counts == s2_counts:
                return True
        
        return False

            

            




