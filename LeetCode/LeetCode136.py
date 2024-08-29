class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap.keys():
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
        for elt in hashmap:
            if hashmap[elt] == 1:
                return elt