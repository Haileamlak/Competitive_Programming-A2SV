# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        head = ListNode()
        if list1.val <= list2.val:
            head = list1
            head.next = self.mergeTwoLists(list1.next, list2)
        
        else:
            head = list2
            head.next = self.mergeTwoLists(list2.next, list1)
        
        return head