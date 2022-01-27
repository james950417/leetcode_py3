# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # ITERATIVE
        result = ListNode()
        result_pointer = result
        while list1 and list2:
            if list1.val >= list2.val:
                result_pointer.next = ListNode(val=list2.val)
                list2 = list2.next
                result_pointer = result_pointer.next
            else:
                result_pointer.next = ListNode(val=list1.val)
                list1 = list1.next
                result_pointer = result_pointer.next
        if list1:
            result_pointer.next = list1
        elif list2:
            result_pointer.next = list2
        return result.next
                   
        
        # # RECURSIVE
        # if list1 is None and list2 is None:
        #     return None
        # elif list1 is None and list2:
        #     return list2
        # elif list1 and list2 is None:
        #     return list1
        # else:
        #     if list1.val >= list2.val:
        #         return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))
        #     else:
        #         return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
