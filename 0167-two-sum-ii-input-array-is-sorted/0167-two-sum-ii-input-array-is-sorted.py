class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        tsum=0
        right=len(numbers)-1
        left=0
        while left<=right:
            tsum=numbers[right]+numbers[left]
            if tsum<target:
                left+=1
            elif tsum>target:
                right-=1
            elif tsum==target:
                return [left+1,right+1]        