class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #if h < len(piles) this would not be possible
        
        piles2 = sorted(piles)
        print(piles2)

        left_p = 0
        right_p = len(piles) - 1
        
        min_safe_rate = piles2[right_p]
        max_unsafe_rate = 1

        #binary search loop
        while left_p <= right_p:
            
            middle_p = (right_p + left_p) // 2
            banana_rate = piles2[middle_p]
            #calculate # of hours for that rate
            num_hours = 0
            for pile in piles2: 
                num_hours += int(math.ceil(pile / banana_rate))
            
            if num_hours == h: 
                max_unsafe_rate = piles2[middle_p]
                min_safe_rate = piles2[middle_p]
                break
            
            if num_hours > h: 
                max_unsafe_rate = piles2[middle_p]
                left_p = middle_p + 1
            else: 
                min_safe_rate = piles2[middle_p]
                right_p = middle_p - 1

        print(max_unsafe_rate)
        print(min_safe_rate)
        while max_unsafe_rate < min_safe_rate: 
            new_rate = (max_unsafe_rate + min_safe_rate) // 2
            num_hours = 0
            for pile in piles: 
                num_hours += int(math.ceil(pile / new_rate))
            
            if num_hours <= h:
                min_safe_rate = new_rate
            else: 
                max_unsafe_rate = new_rate + 1
        
        return min_safe_rate

        
        