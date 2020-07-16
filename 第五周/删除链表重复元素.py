class LinkList(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(head): # 删除的是重复的结点
    if not head: return head
    dummy = LinkList(0)
    dummy.next = head
    cur = head
    while cur: # 因为事先不知道哪些元素是重复的，因此要逐一循环遍历来做
        # 全部删除完再移动到下一个元素
        while cur.next and cur.val == cur.next.val:
            cur.next = cur.next.next
        cur = cur.next
    return dummy.next

def reverseList(head): # 链表反转
    if not head or not head.next: return head
    cur = None
    pre = head
    while pre:
        tmp = LinkList(pre.val) # 若直接 pre.next = cur 会断链，因为改变了pre之前的指向
        tmp.next = cur # 相当于在另一个副本链表上操作
        cur = tmp
        pre = pre.next
    return pre

def recursionReverseLink(head): # 递归的方式反转链表
    if not head or not head.next: return head
    p = recursionReverseLink(head.next)
    head.next.next = head # head.next 是 head 的下一个结点   让其指向 head 即可反转
    head.next = None # head 指向空 实际上是第n+1个结点
    return p # 返回新的头结点 理解p的含义

def reverseN(head, n): # 反转前N个结点(N小于等于链表长度)
    nonlocal successor
    if n == 1:
        successor = head.next # 记录第n+1个结点
        return head
    p = reverseN(head.next, n-1) # 以head.next为起点 需要反转前n-1个结点
    head.next.next = head
    head.next = successor
    return p

def reverseM2N(head, m, n): # 反转从m到n这一段链表(局部反转)
    if m == 1: # m=1 就相当于反转前n个结点
        return reverseN(head, n)
    p = reverseM2N(head.next, m-1, n-1)
    head.next = p # 这个操作只是连接反转前面的部分了 反转后后面那部分没有接上 断链了 待优化
    return head # 尝试了几次连接后面的不是很完美

