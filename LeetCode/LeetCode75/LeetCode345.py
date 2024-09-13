class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        vowels = 'aeiouAEIOU'
        vowel_order = []
        for i in range(len(chars)):
            if chars[i] in vowels:
                vowel_order.append(chars[i])
        idx = len(vowel_order) - 1
        for i in range(len(chars)):
            if chars[i] in vowels:
                chars[i] = vowel_order[idx]
                idx -= 1
        return "".join(chars)