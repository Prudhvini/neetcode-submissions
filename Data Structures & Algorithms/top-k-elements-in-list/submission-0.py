class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = 1+freq_map.get(num,0)
        
        arr = []
        for num,cnt in freq_map.items():
            arr.append([cnt, num])
        arr.sort()

        result = []
        for i in range(k):
            result.append(arr.pop()[1])
        
        return result
