# print(False and False) # 输出的是 False
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        cur = None # 在前
        pre = head # 在后  相对于链表原始顺序来说的
        # 先反转链表
        while pre:
            temp = ListNode(pre.val)
            temp.next = cur
            cur = temp # (1)(2)类似于交换操作，交换之前需要引入中间变量(类似数组)
            pre = pre.next # 更新状态，指针往前移
        # 不知道为什么 我采用递归反转链表 有的测试用例没通过 已经测试过，递归反转写法没啥问题
        # def reverseLink(head):
        #     if not head or not head.next:
        #         return head
        #     p = reverseLink(head.next)
        #     head.next.next = head
        #     head.next = None
        #     return p
        # 再一一比较元素
        while cur and head:
            if cur.val != head.val:
                return False
            else:
                cur = cur.next
                head = head.next
        return cur == None and head == None