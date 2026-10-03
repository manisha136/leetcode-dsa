class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        tsum=0
        record=[]
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1

            
            
            if i>0 and nums[i]==nums[i-1]:
                continue

            while left<right: 
                tsum=nums[i]+nums[left]+nums[right]

                if tsum<0:
                    left+=1
                elif tsum>0:
                    right-=1
                else:
                    record.append([nums[i],nums[left],nums[right]])   

                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1  
                    while right>left and nums[right]==nums[right+1]: 
                        right-=1
        return record                               