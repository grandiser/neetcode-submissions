class Solution:

    def encode(self, strs: List[str]) -> str:
        one_string = ""

        for s in strs:
            one_string += (s + '\n')
        
        return one_string

    def decode(self, s: str) -> List[str]:
        
        strs = s.split('\n')
        return strs[:-1]