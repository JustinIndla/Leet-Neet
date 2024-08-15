class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_out = {}
        list_out = []
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        for word in strs:
            breakdown = [0] * 26
            for i in range(len(word)):
                char = word[i]
                breakdown[alpha.find(char)] = breakdown[alpha.find(char)] + 1
                print(breakdown)
            breakdown = " ".join(map(str, breakdown))
            print(breakdown)
            if breakdown not in hash_out.keys():
                hash_out[breakdown] = [word]
            else:
                hash_out[breakdown].append(word)
        print(hash_out)
        for breakdown in hash_out:
            list_out.append(hash_out[breakdown])
        return list_out