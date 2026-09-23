class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}
        max_length=0
        window_length=0
        max_frequency=0
        left=0

        for right,current in enumerate(s):

            if current in freq:
                freq[current]+=1
            else:
                freq[current]=1 

            window_length=right-left+1
            max_frequency=max(max_frequency,freq[current]) 
            while window_length-max_frequency>k:
                current=s[left]
                freq[current]-=1
                left+=1
                window_length=right-left+1
            max_length=max(max_length,right-left+1)    

        return max_length    