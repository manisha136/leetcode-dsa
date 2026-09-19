class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        zero_count=0
        left=0
        max_length=0
        for right,current in enumerate(nums):
            if current==0:
                zero_count+=1
            while zero_count>k:
                if nums[left]==0:
                   zero_count-=1
                left+=1
            max_length=max(max_length,right-left+1)   

        return max_length        