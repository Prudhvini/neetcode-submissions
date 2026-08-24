class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for i in nums:
            if i in freq_map:
                freq_map[i]+=1
            else:
                freq_map[i]=1

        arr = []
        for num,cnt in freq_map.items():
            arr.append([cnt,num])
        arr.sort()

        result = []
        for i in range(k):
            result.append(arr.pop()[1])
        return result
        