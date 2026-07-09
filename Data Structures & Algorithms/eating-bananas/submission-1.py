class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high

        while low <=high:
            speed = low + (high-low) // 2
            
            total_hours = 0
            for i in piles:
                hours = (i + speed -1) // speed
                total_hours += hours
            if total_hours <= h :
                ans = speed
                high= speed - 1
            else:
                low = speed + 1
        return ans