class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        A = [0] * len(s)
        hash_idx = {}
        A[0] = 1
        hash_idx[s[0]] = 0
        for i in range(1, len(s)):
            if s[i] not in hash_idx.keys():
                A[i] = 1 + A[i-1]
                hash_idx[s[i]] = i
            else:
                A[i] = i - hash_idx[s[i]]
                poppable = []
                for char in hash_idx:
                    if hash_idx[char] < hash_idx[s[i]]:
                        poppable.append(char)
                for elt in poppable:
                    hash_idx.pop(elt)
                hash_idx[s[i]] = i
        return max(A)