class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 合并两个链表 -> 顺序合并
# def mergeTwoList(a:ListNode, b:ListNode) -> ListNode:
#     if not a: return b
#     if not b: return a
#     dummy = ListNode(0) # 哑点 # 若head = None 则return head即可
#     tail = dummy
#     while(a and b):
#         if(a.val < b.val):
#             tail.next = a
#             a = a.next # 更新a # 这里的更新有点类似于归并排序那里的更新 思路一样
#         else:
#             tail.next = b
#             b = b.next # 更新b
#         tail = tail.next # 更新tail
#     if not a: tail.next = b
#     if not b: tail.next = a
#     return dummy.next # 因为head前定义了一个哑点
# 合并两个链表 -> 递归合并
def mergeTwoList(a:ListNode, b:ListNode) -> ListNode:
    if not a: return b
    if not b: return a
    if a.val < b.val:
        a.next = mergeTwoList(a.next, b)
        return a
    else:
        b.next = mergeTwoList(a, b.next)
        return b
# 合并K个链表 -> 顺序
# def mergeKList(lists:[ListNode]) -> ListNode:
#     ans = None
#     n = len(lists)
#     for i in range(n):
#         ans = mergeTwoList(ans, lists[i])
#     return ans
# 合并K个链表 -> 归并
def mergeKList(lists:[ListNode]) -> ListNode:
    return merge(lists, 0, len(lists) - 1)
def merge(lists:[ListNode], left:int, right:int) -> ListNode:
    if left == right: return lists[left]
    mid = int((left + right) / 2)
    return mergeTwoList(merge(lists, left, mid), merge(lists, mid+1, right))
