class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        for i in range(0, len(nums)):
            num_needed = target - nums[i]
            if num_needed in checked.keys():
                return [i, checked[num_needed]]
            checked[nums[i]] = i

#         num_index_map = {}
#         for i in range(0, len(nums)):
#             if nums[i] in num_index_map.keys():
#                 num_index_map[nums[i]].append(i)
#             else:
#                 num_index_map[nums[i]] = [i]
        
#         for j in range(0, len(nums)):
#             num_needed = target - nums[j]
#             if num_needed in num_index_map.keys():
#                 if num_needed != nums[j]:
#                     return [j, num_index_map[num_needed][0]]
#                 else:
#                     if len(num_index_map[num_needed]) > 1:
#                         return num_index_map[num_needed]
