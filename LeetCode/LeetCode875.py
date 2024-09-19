import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(k):
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            return time <= h

        left = 1
        right = max(piles)
        mid = 0

        valid = -1
        while left <= right:
            mid = (right + left) // 2
            if check(mid):
                valid = mid
                right = mid-1
            else:
                left = mid+1
        return valid