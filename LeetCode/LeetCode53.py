class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        A = [None] * len(nums)
        A[0] = nums[0]
        for i in range(1, len(nums)):
            A[i] = max(nums[i], nums[i] + A[i-1])
        return max(A)