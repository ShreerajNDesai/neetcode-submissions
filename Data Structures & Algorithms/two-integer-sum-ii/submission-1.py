class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left <= right:
            if left == right:
                left +=  1
                right = len(numbers)-1
            if numbers[left] + numbers[right] == target:
                result  = [left+1,right+1]
                return result
            else:
                right -= 1
