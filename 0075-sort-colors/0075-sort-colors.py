class Solution:
    def sortColors(self, nums: list[int]) -> None:
        count=[0]*(max(nums)+1)
        index=0
        for i in range(len(nums)):
            current=nums[i]
            count[current]+=1
        for i in range(len(count)):
            for j in range(count[i]):
                nums[index]=i
                index+=1    
        