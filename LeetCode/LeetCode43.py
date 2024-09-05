class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        nums = '0123456789'

        n1 = 0
        n2 = 0

        for i in range(len(num1)):
            n1 += nums.find(num1[i]) * (10 ** (len(num1[i:len(num1)]) - 1))

        for i in range(len(num2)):
            n2 += nums.find(num2[i]) * (10 ** (len(num2[i:len(num2)]) - 1))

        prod = n1 * n2
        prod_str = ''
        if prod == 0:
            return "0"

        while prod > 0:
            prod_str += nums[prod % 10]
            prod = prod // 10
        return prod_str[::-1]