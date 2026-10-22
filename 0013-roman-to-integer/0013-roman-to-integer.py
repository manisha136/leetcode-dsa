class Solution:
    def romanToInt(self, s: str) -> int:
        roman={}

        roman['I']=1
        roman['V']=5
        roman['X']=10
        roman['L']=50
        roman['C']=100
        roman['D']=500
        roman['M']=1000

        result=0


        for i in range(len(s)-1):
            current=s[i]
            nexts=s[i+1]
            if roman[current]<roman[nexts]:
               result-=roman[current]
            else:
               result+=roman[current]    
        result+=roman[s[-1]]
        return result 
        