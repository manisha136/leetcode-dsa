class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq={}
        left=0
        max_length=0
        for right in range(len(s)):
            current=s[right]
            if current in freq:
                freq[current]+=1
            else:
                freq[current]=1
                    
            while freq[current]>1:
                  freq[s[left]]-=1
                  left+=1

            max_length=max(max_length,right-left+1)

        return max_length
                   
