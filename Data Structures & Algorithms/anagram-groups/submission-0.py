class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_map = {}

        for in_str in strs:
            str_letters = [0] * 26
            for letter in in_str:
                str_letters[ord(letter) - ord('a')] += 1

            str_tuple = tuple(str_letters)   
            if str_tuple in dict_map:
                dict_map[str_tuple].append(in_str)
            else:
                dict_map[str_tuple] = [in_str]

        return list(dict_map.values())







