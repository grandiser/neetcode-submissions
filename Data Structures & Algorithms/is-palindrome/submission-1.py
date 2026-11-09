class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9'}

        l, r = 0, len(s) - 1
        s = s.lower()

        while l <= r:
            if s[l] in alphabet and s[r] in alphabet:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            elif s[l] not in alphabet:
                l += 1
            elif s[r] not in alphabet:
                r -= 1
        
        return True


            
        

            
            
