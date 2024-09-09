class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {4: ['IV', 'XL', 'CD'], 
                5: ['V', 'L', 'D'], 9: ['IX', 'XC', 'CM']}
        ones = ['I', 'X', 'C', 'M']
        out = ''
        exp = 3
        while exp >= 0:
            digit = num // (10 ** exp)
            if digit in mapping.keys():
                out += mapping[digit][exp]
            else:
                if digit >= 5:
                    out += mapping[5][exp]
                    digit -= 5
                for i in range(digit):
                    out += ones[exp]
            num %= (10 ** exp)
            exp -= 1
        return out