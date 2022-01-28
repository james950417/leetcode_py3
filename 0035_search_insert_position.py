class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1
        while left_pointer <= right_pointer:
            mid_pointer = (left_pointer + right_pointer) // 2
            if nums[mid_pointer] == target:
                return mid_pointer
            elif nums[mid_pointer] < target:
                left_pointer = mid_pointer + 1
            else:
                right_pointer = mid_pointer - 1
        return left_pointer

