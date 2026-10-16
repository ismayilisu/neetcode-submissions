class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr=float("-inf")
        maxi=float("-inf")
        for i in range(len(nums)):
            curr=max(nums[i],curr+nums[i])
            maxi=max(maxi,curr)
        return maxi