class Solution:
    def isPalindrome(self, s: str) -> bool:
        right=len(s)-1
        left=0

        while left<right: 

            while left<=right and not s[left].isalnum():
                left+=1
            while right>=left and  not s[right].isalnum() : 
                right-=1

            if left<=right and s[left].lower()!=s[right].lower() :
               return False
        
    
            right-=1
            left+=1
          

    
        return True