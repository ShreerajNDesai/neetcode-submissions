class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = (sorted(nums))
        count = [1]
        if len(nums) > 0:
            for i in range(0,len(nums)-1):
                if nums[i+1] == nums[i]+1:
                    count[0] += 1
                elif nums[i+1] == nums[i]:
                    continue
                else: 
                    count.insert(0,1) 
        else:
            return 0
        return max(count)