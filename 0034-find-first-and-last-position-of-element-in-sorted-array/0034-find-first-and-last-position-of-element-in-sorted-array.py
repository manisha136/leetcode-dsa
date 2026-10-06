class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def binary_search(find_first):
            right=len(nums)-1
            left=0
            answer=-1

            while left<=right:
                mid=(left+right)//2

                if nums[mid]>target:
                    right=mid-1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    answer=mid

                    if find_first:
                        right=mid-1
                    else:
                        left=mid+1 

            return answer     
        first=binary_search(True) 
        last=binary_search(False)   

        return [first,last]

        