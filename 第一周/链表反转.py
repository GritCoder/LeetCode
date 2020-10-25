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
    cur = head
    pre = None
    while cur:
        # 好好理解中间变量(副本)的含义
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    # 反转后的新的头结点
    return pre
# 也可以递归实现, 知道就行了，不在这里写了
def recursion(head):
    # 递归结束条件
    if not head or not head.next:
        return head
    # 新的头结点
    p = reverseList(head.next)
    head.next.next = head
    head.next = None
    return p
'''
递归的执行过程理解一下
reverseList: head=1
    reverseList: head=2
         reverseList: head=3
            reverseList:head=4
                # 个人理解，当head=4的时候，递归就已经返回了，因为参数传的是head.next
                ### reverseList:head=5 ### 
            4.next.next = 4，即5.next = 4, 4.next = None，实现了一次局部反转，此时p = 5，局部链表是5->4->None
                再往下，4是怎么来的呢？在参数中，3.next = 4，因此递归再往下走的时候，就是
                3.next.next = 3,即4.next = 3, 3.next = None，实现了一次局部反转，此时p = 5，局部链表是5->4->3->None
                    以此类推.....，直到整个链表反转结束，return p ，即 5 
'''