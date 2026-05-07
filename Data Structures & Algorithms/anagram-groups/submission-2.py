class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagrams: order doesnt matter
        # care about: # letters

        # createa  dcit
        # key by letter count
        # for same keys, that means we have the same word (anagram)
        # append to list of words
        # return list(dict())

        anagrams = defaultdict(list)

        for word in strs:
            letters = [0] * 26
            for letter in word:
                idx = ord(letter) - ord('a')
                letters[idx] += 1
            anagrams[tuple(letters)].append(word)

        return list(anagrams.values())