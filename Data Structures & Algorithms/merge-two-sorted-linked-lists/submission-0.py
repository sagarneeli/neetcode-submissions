# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_head = ListNode()
        head1 = list1
        head2 = list2
        res = merged_head

        while head1 and head2:
            if head1.val < head2.val:
                merged_head.next = head1
                head1 = head1.next
            else:
                merged_head.next = head2
                head2 = head2.next
            
            merged_head = merged_head.next
        
        while head1:
            merged_head.next = head1
            head1 = head1.next
            merged_head = merged_head.next

        while head2:
            merged_head.next = head2
            head2 = head2.next
            merged_head = merged_head.next

        return res.next

        