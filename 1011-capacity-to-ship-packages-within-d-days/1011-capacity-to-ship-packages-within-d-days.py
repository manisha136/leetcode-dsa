class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        answer=0

        while left<=right:
            capacity=(left+right)//2
            shipdays=1
            current_weight=0
            for weight in weights:
                if current_weight+weight<=capacity:
                    current_weight+=weight
                else:
                    current_weight=weight
                    shipdays+=1
            if shipdays<=days:
                answer=capacity
                right=capacity-1
            else:
                left=capacity+1
        return answer            


        