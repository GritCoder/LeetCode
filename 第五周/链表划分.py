class LinkList(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def createList(self, lis):
        head = LinkList(lis[0]) # 创建头结点
        p = head
        for i in range(1, len(lis)):
            node = LinkList(lis[i]) # 申请一个结点
            p.next = node # 连接
            p = p.next # 指针后移
        return head # 返回head就行  因为head没有移动  移动的是 p
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前
# 思路：将大于x的节点，放到另外一个链表，最后连接这两个链表
# 注意，题目只是要求小于x的排在x之前，没有限制大于x的，即大于x的并且在x前面的不用考虑
def partition(head, x):
    if not head: return head
    head_dummy = LinkList(0) # 创建哑结点 辅助作用
    head_dummy.next = head  # 返回用
    tail_dummy = LinkList(0)
    tail = tail_dummy # 拼接用的
    head = head_dummy
    while head.next: # 注意 head.next指向的是头结点(head此时是哑结点)
        if head.next.val < x:
            head = head.next
        else:
            tmp = head.next # 必须创建临时结点 不然tail的指向会出现错误
            head.next = head.next.next # 跳过该结点(删除)
            tail.next = tmp # 因为tail是哑结点 所以tail.next指向的是新链表的第一个结点
            tail = tail.next

    tail.next = None #
    # 拼接两个链表
    head.next = tail_dummy.next # 不能指向tail 因为tail已经改变了 不再指向第一个结点
    return head_dummy.next

lis = [1,2,3,4,5]
obj = LinkList(66) # 是66还是其他值对结果没有任何影响 因为这个仅仅是用来创建对象
head = obj.createList(lis)
while head:
    print(head.val)
    head = head.next