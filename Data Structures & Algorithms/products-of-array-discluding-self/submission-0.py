class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        size = len(nums)
        suffix = [0] * size
        prefix = [0] * size
        
        prefix[0] = 1
        suffix[size-1] = 1
        for i in range(1,size):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(size-2, -1,-1):
            suffix[i] = nums[i+1]*suffix[i+1]

        product = [0] * size
        for i in range(size):
            product[i] = prefix[i]*suffix[i]
        
        return product