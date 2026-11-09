class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            bucket = [0] * 26
            for l in s:
                bucket[ord(l) - ord('a')] += 1
            
            bucket = tuple(bucket)
            anagrams[bucket].append(s)

        return list(anagrams.values())
            
