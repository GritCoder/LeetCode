class listNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 二次遍历法
# def removeLinkNode(head, n):
#     if head == None:
#         return
#     length = 0
#     dummy = listNode(0) # 不能直接返回head,因为head在程序处理后就发生改变了
#     dummy.next = head # 哑结点用来简化某些极端情况 同时也记录head的起始信息并返回
#     first = head
#     # 先求链表长度
#     while first:
#         first = first.next
#         length += 1
#     length -= n
#     first = dummy # 注意此时first并没有指向head,而是head的前驱
#     while length > 0: # 因此移动length次,若first=head,则移动length-1次到前驱节点
#         length -= 1
#         first = first.next
#     # 此时first已经指向n节点的前驱节点
#     first.next = first.next.next
#     return dummy.next

# 一次遍历 双指针法,有一定技巧
'''
第一个指针从列表的开头(指向头，而非dummy)向前移动 n(若指向dummy,则移动n+1) 步，
而第二个指针将从列表的开头出发。
我们通过同时移动两个指针向前来保持这个恒定的间隔，直到第一个指针到达最后一个结点。
此时第二个指针将指向从最后一个结点数起的第 n 个结点。
我们重新链接第二个指针所引用的结点的 next 指针指向该结点的下下个结点。
'''

# 链表的题目比较抽象,执行的时候可以先画个草图,太有用了！！！
def removeLinkNode(head, n):
    if head == None:
        return
    dummy = listNode(0)
    dummy.next = head
    first = dummy
    for i in range(n):
        first = first.next
    second = dummy
    while first.next:
        first = first.next
        second = second.next
    second.next = second.next.next # 正好指向n的前驱节点
    return dummy.next