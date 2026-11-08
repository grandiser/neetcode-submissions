class Solution:
    def longestPalindrome(self, s: str) -> str:
        # abba = 4
        # racecar = 7
        # soosxmomom = 5

        # ababd
        # len(s) = 5
        # l,r = 0, 2
        # curlen = 1
        # ans = a
        # 
        bl = 0
        ans = ""

        for i in range(len(s)): 

            for l,r in [(i,i), (i, i+1)]:

                while l >= 0 and r < len(s) and s[l] == s[r]:
                    curlen = r-l+1

                    if curlen > bl:
                        bl = curlen
                        ans = s[l:r+1]

                    l -= 1
                    r += 1
            
        return ans

