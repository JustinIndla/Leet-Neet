class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        min_word = str1 if len(str1) < len(str2) else str2
        end = len(min_word)
        while end > 0:
            tmp = min_word[0:end]
            print(tmp)
            if((tmp * (len(str1) // len(tmp)) == str1) and (tmp * (len(str2) // len(tmp)) == str2)):
                return tmp
            end -= 1
        return ''