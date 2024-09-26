class Solution:
    def countBits(self, n: int) -> List[int]:
        A = [0] * (n+1)
        for i in range(n+1):
            A[i] = str(bin(i)).count('1')
        return A