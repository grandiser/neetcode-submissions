class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_table = {}
        t_table = {}

        for letter in s:
            if letter not in s_table:
                s_table[letter] = 1
            else:
                s_table[letter] += 1
        
        for letter in t:
            if letter not in t_table:
                t_table[letter] = 1
            else:
                t_table[letter] += 1
        
        return s_table == t_table