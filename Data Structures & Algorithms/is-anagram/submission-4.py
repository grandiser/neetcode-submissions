class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_c = defaultdict(int)
        s_t = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            s_c[s[i]] += 1
            s_t[t[i]] += 1
        
        return s_c == s_t