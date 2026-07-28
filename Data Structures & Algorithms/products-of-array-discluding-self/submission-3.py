class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0)<2:
            output = []
            for i in range(len(nums)):
                prod = 1
                for j in range(len(nums)):
                    if j!=i:
                        prod *= nums[j]
                output.append(prod)
            return output
        nums = [0]*len(nums)
        return nums