class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += f"{len(s)}#{s}"
        
        return encoded

    def decode(self, s: str) -> List[str]:
        
        decoded = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

#      4#neet4#code4#love3#you

            w_len = int(s[i:j])
            j += 1
            
            decoded.append(s[j:j+w_len])

            i = j+w_len
        return decoded



