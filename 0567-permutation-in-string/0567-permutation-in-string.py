class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
           return False
        freq_s1={}
        freq_win={}
        for current in s1:
            if current in freq_s1:
                freq_s1[current]+=1
            else:
                freq_s1[current]=1
        for i in range(len(s1)):
            current=s2[i]
            if current in freq_win:
                freq_win[current]+=1
            else:
                freq_win[current]=1
            if freq_win==freq_s1:
               return True
        for right in range(len(s1),len(s2)):
            outgoing=s2[right-len(s1)]  
            incoming=s2[right]
            freq_win[outgoing]-=1
            if freq_win[outgoing]==0:
                del freq_win[outgoing]
            if incoming in freq_win:
                freq_win[incoming]+=1
            else:
                freq_win[incoming]=1
            if freq_win==freq_s1:
               return True
        return False                                       

        