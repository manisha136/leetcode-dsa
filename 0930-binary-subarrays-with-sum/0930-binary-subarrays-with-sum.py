class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        prefix_sum=0
        needed=0
        count=0
        freq={0:1}
        for current in nums:
            prefix_sum+=current

            needed=prefix_sum-goal

            if needed in freq:
                count+=freq[needed]

            if prefix_sum in freq:
                freq[prefix_sum]+=1
            else:
                freq[prefix_sum]=1    
        return count      

        