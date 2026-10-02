class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        prefix_sum=0
        count=0
        needed=0
        freq={0:1}

        for current in nums:
            current=1 if current%2!=0 else 0
            prefix_sum+=current

            needed=prefix_sum-k

            if needed in freq:
               count+=freq[needed]

            if prefix_sum in freq:
                freq[prefix_sum]+=1
            else:
                freq[prefix_sum]=1
        return count                
