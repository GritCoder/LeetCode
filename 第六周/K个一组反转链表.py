class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
# 反转一个子链表 返回新的头与尾
def reverse(head, tail):
    prev = tail.next # 尾的后继 返回的时候实际上是新的前驱了
    p = head
    while prev != tail: # 实际演示一遍，一开始prev指向tail.next 然后是head 然后 head.next ... 当指向到tail时 说明一圈反转完成了
        nex = p.next # 提前记录下一个结点 否则指针指向就改变了
        p.next = prev # 其实本质上类似于链表插入的操作
        prev = p # 更新prev 确保prev始终指向新的tail(知道这个意思就行了)
        p = nex # 头指针后移
    return tail, head # 新的头与尾 实际上返回的尾是尾的前驱 因为下面while循环里是 pre = tail
# 其实跟正常的反转 代码都类似 关键是每次反转前要记录下头的前驱和尾的后继 连接用
def reverseK(head, k):
    dummy = ListNode(-1)
    dummy.next = head
    pre = dummy # 头的前驱
    while head:
        tail = pre
        # 查看剩余部分长度是否大于等于 k
        for i in range(k):
            tail = tail.next
            if not tail:
                return dummy.next
        nex = tail.next # 这里实际上是头结点
        head, tail = reverse(head, tail)
        # 把子链表重新接回原链表
        pre.next = head # 接头
        tail.next = nex # 接尾
        pre = tail # 更新新的头结点的前驱 理解 tail 本质上是新的前驱
        head = tail.next # 更新新的头结点
    return dummy.next

# 大概思想
# 记录头前驱
# 判断长度是否大于等于 k
# 去反转(反转里面记录一下尾的后继)
# 返回反转结果并拼接
# 更新头结点 后移 继续反转