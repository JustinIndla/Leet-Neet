class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)

        out = ''

        for i in range(len1 + len2):
            if i // 2 >= len1:
                out += word2[i - len1]
            elif i // 2 >= len2:
                out += word1[i - len2]
            else:
                if i % 2 == 1:
                    out += word2[i // 2]
                else:
                    out += word1[i // 2]
            print(i, out)
        return out