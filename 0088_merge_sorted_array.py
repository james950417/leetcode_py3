class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            if n != 0:
                nums1[:] = nums2
        else:
            if n != 0:
                del nums1[m:]
                nums1_pointer = 0
                nums2_pointer = 0
                while nums1_pointer < len(nums1) and nums2_pointer < len(nums2):
                    if nums1[nums1_pointer] <= nums2[nums2_pointer]:
                        nums1_pointer += 1
                    else:
                        nums1[:] = nums1[:nums1_pointer] + [nums2[nums2_pointer]] + nums1[nums1_pointer:]
                        nums1_pointer += 1
                        nums2_pointer += 1
                if nums2_pointer < len(nums2):
                    nums1 += nums2[nums2_pointer:]
