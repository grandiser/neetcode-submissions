class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best_k = float('inf')
        all_bananas = sum(piles)

        while l <= r:
            k = (l+r)//2
            time_remaining = h

            for pile in piles:
                time_for_pile = math.ceil(pile / k)
                time_remaining -= time_for_pile
            
            if time_remaining >= 0:
                best_k = min(k, best_k)
                r = k - 1
            else:
                l = k + 1
    
        return best_k


