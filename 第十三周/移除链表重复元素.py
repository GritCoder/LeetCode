# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 这个是有序链表元素的移除，如果是无序的，要多一项判断，因为说不定哪个元素是重复的，双循环了
class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None
        slow, fast = head, head
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        slow.next = None
        return head