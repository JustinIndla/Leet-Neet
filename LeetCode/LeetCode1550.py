class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consecutive = 0
        for i in arr:
            if i % 2 == 1:
                consecutive += 1
            else:
                consecutive = 0
            if consecutive == 3:
                return True
        return False