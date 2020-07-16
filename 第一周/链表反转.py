class LinkNode:
    def __init__(self, x, next=None):
        self.val, self.next = x, next
'''
好理解的双指针
定义两个指针： pre 和 cur ；pre 在前 cur 在后。
每次让 pre 的 next 指向 cur ，实现一次局部反转
局部反转完成之后， pre 和 cur 同时往前移动一个位置
循环上述过程，直至 pre 到达链表尾部
'''
def reverseList(head: LinkNode) -> LinkNode:
    cur = None
    pre = head
    while pre:
        # 好好理解中间变量(副本)的含义
        temp = LinkNode(pre.val) # 若没有此行，直接执行下面三句，会导致断链报错
        temp.next = cur # (1)
        cur = temp # (2)   (1)(2)类似于交换操作，交换之前需要引入中间变量(类似数组)
        pre = pre.next # 更新状态，指针往前移
    return cur
# 也可以递归实现, 知道就行了，不在这里写了