class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left=1
        right=max(piles)
        answer=0
        while left<=right:
            mid=(left+right)//2
            k=0
            for pile in piles:
                current=(pile+mid-1)//mid
                k+=current
            if k<=h:
                answer=mid
                right=mid-1
            else:
                left=mid+1
        return answer           
        