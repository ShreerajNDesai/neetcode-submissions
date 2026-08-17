class Solution:
    def search(self, nums: List[int], target: int) -> int:

        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[L]:
                # we are in the left half
                if target >= nums[L] and target < nums[mid]:
                    # we can go left
                    R = mid - 1
                else:
                    # we should go to the right half
                    L = mid + 1
            else:
                # we are in the right half
                if target > nums[R] or target < nums[mid]:
                    # we should go left
                    R = mid - 1
                else:
                    # we can go right
                    L = mid + 1
        
        return -1


        