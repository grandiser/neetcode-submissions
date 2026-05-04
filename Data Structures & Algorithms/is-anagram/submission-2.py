class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_table = {}
        t_table = {}

        for letter in s:
            if s_table.get(letter):
                s_table[letter] += 1
            else:
                s_table[letter] = 1
        
        for letter in t:
            if t_table.get(letter):
                t_table[letter] += 1
            else:
                t_table[letter] = 1
        
        return s_table == t_table
        