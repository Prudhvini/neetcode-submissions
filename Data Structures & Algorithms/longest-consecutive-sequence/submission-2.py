class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_count = 1
        nums_set = set(nums)
        count = 0
        for n in nums_set:
            if n-1 not in nums_set:
                count = 1
                while n+1 in nums_set:
                    count+=1
                    n = n+1
                max_count = max(count, max_count)
                count = 0
        return max_count