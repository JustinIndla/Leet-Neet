class Solution:
    def reverseBits(self, n: int) -> int:
        str_n = str(bin(n))[2:]
        str_n = (32 - len(str_n)) * '0' + str_n
        str_n = str_n[::-1]
        return(int(str_n, 2))
        