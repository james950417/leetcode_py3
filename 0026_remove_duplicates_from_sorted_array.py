class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        curr_num = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == curr_num:
                nums.pop(i)
            else:
                curr_num = nums[i]
                i += 1
        return len(nums)
