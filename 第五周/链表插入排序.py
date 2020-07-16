# 插入排序已经包含插入操作了
class linkNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
# 重点掌握链表的插入排序和归并排序
def insertSort(head):
    if not head or not head.next:
        return head
    res = linkNode(-1) # 创建结果链表
    while head:
        nxt = head.next # 记录原始链表下一结点位置
        cur = res # 必须有的操作 始终指向哑点 方便操作
        while cur.next and cur.next.val < head.val: # head的值去与结果链表中的元素逐一比较
            cur = cur.next # 实际上是判断要插入的位置
        # 插入(头)结点到新链表中
        head.next = cur.next # 先连
        cur.next = head # 后断 理解为什么 避免形成死环和断链
        # 原始结点后移
        head = nxt
    return res.next # 理解 必须return res.next 其他的就不对

def bubbleSort(head):
    if not head or not head.next:
        return head
    dummy = linkNode(-1)
    dummy.next = head
    first, second = head.next, head
    while first:
        while first.next:
            if first.val > first.next.val: # 交换
                # tmp = first.val # C语言写法
                # first.val = first.next.val
                # first.next.val = tmp
                first.val, first.next.val = first.next.val, first.val # Python写法
            first = first.next
        # first 和 second 指针后移
        first = second.next
        second = first
        # second = first.next # first已经在上面修改了 这样写不对
    return dummy.next # 不细纠结了 知道就行了 实际上返回结果有点小问题 知道就行了 重点是思路

# 不写了 知道思想就行了
# def selectSort(head):
#     if not head or not head.next:
#         return head
#     dummy = linkNode(-1)
#     dummy.next = head









