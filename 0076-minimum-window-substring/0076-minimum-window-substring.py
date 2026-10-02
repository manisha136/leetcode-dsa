class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window={}
        need={}
        left=0
        start=0
        min_length=float('inf')
        formed=0
        
        for current in t:
            if current in need:
                need[current]+=1
            else:
                need[current]=1
        for right,current in enumerate(s):
            if current in window:
                window[current]+=1
            else:
                window[current]=1
            if current in need and window[current]==need[current]:
                formed+=1
            while len(need)==formed:
                current=s[left]
                
                window_length=right-left+1
                if window_length<min_length:
                    min_length=window_length
                    start=left

                window[current]-=1

                if current in need and window[current]<need[current]:
                    formed-=1
                left+=1    
        if min_length==float('inf'):
           return ""
        else:
           return s[start:start+min_length]    

