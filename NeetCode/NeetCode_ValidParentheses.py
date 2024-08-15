class Solution:
    def isValid(self, s: str) -> bool:
        complements = {'}': '{', ')': '(', ']': '['}
        stack = []
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            elif s[i] in [')', '}', ']']:
                if stack == []:
                    return False
                elif stack[-1] == complements[s[i]]:
                    stack.pop()
                else:
                    return False
        return stack == []