class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        result = []
        while l<r:
            total = numbers[l]+numbers[r]
            if total == target:
                result.append(l+1)
                result.append(r+1)
                return result
            elif total<target:
                l+=1
            else:
                r-=1
        
        return result