class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left=0
        freq={}
        max_length=0

        for right,current in enumerate(fruits):
            if current in freq:
                freq[current]+=1
            else:
                freq[current]=1
            while len(freq)>2:
                current=fruits[left] 
                freq[current]-=1
                if freq[current]==0:
                   del freq[current]
                left+=1

            max_length=max(max_length,right-left+1)
        return max_length              

                
