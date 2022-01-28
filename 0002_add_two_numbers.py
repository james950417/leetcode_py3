# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        result_pointer = result
        carryover = 0
        while l1 and l2:
            temp_sum = l1.val + l2.val + carryover
            new_digit, carryover = self.determine_carryover(temp_sum)
            result_pointer.next = ListNode(val=new_digit)
            l1 = l1.next
            l2 = l2.next
            result_pointer = result_pointer.next
        if l1 and l2 is None:
            while carryover != 0 and l1:
                temp_sum = l1.val + carryover
                new_digit, carryover = self.determine_carryover(temp_sum)
                result_pointer.next = ListNode(val=new_digit)
                l1 = l1.next
                result_pointer = result_pointer.next
            if l1:
                result_pointer.next = l1
        elif l1 is None and l2:
            while carryover != 0 and l2:
                temp_sum = l2.val + carryover
                new_digit, carryover = self.determine_carryover(temp_sum)
                result_pointer.next = ListNode(val=new_digit)
                l2 = l2.next
                result_pointer = result_pointer.next
            if l2:
                result_pointer.next = l2
        if carryover == 1:
            result_pointer.next = ListNode(val=1)
        return result.next
    
    def determine_carryover(self, temp_sum: int) -> (int, int):
        """
        Helper function that takes in a sum of two integers and determine the new digit as well as if carryover is needed.
        """
        if temp_sum >= 10:
            new_digit = temp_sum - 10
            carryover = 1
        else:
            new_digit = temp_sum
            carryover = 0
        return (new_digit, carryover)
