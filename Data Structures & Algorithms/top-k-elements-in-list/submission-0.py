class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        count = {}

        for num in nums:
            if count.get(num):
                count[num] += 1
            else:
                count[num] = 1
        
        for n, c in count.items():
            freq[c].append(n)
        
        return_list = []
        for n_freq in freq[::-1]:
            for n in n_freq:
                return_list.append(n)
                if len(return_list) == k:
                    return return_list


        