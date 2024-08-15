class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for elt in nums:
            if elt in counts.keys():
                counts[elt] += 1
            else:
                counts[elt] = 1
        k_most = [(' ', 0)] * k
        min_k_count = min(list(map(lambda x: x[1], k_most)))

        def findCount(list_in, num):
            for i in range(len(list_in)):
                if list_in[i][1] == num:
                    return i
            return -1

        for elt in counts:
            if counts[elt] > min_k_count:
                k_most[findCount(k_most, min_k_count)] = (elt, counts[elt])
                min_k_count = min(list(map(lambda x: x[1], k_most)))
        return list(map(lambda x: x[0], k_most))