class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        left=nums[0:mid]
        right=nums[mid:]
        sorted_right=self.sortArray(right)
        sorted_left=self.sortArray(left)
        i=0
        j=0
        merged=[]

        while i<len(sorted_left) and j<len(sorted_right):
            if sorted_left[i]<=sorted_right[j]:
                merged.append(sorted_left[i])
                i+=1
            else:
                merged.append(sorted_right[j])
                j+=1

        while i<len(sorted_left):
            merged.append(sorted_left[i])
            i+=1

        while j<len(sorted_right):
            merged.append(sorted_right[j])
            j+=1

        return merged            

