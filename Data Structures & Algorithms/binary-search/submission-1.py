class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,hi = 0,len(nums)-1

        while lo <= hi:
            mid = (lo+hi)//2
            midval = nums[mid]

            if midval == target:
                return mid
            elif target < midval:
                hi = mid - 1
            elif target > midval:
                lo = mid + 1
        return -1
        
