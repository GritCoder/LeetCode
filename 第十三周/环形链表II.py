# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null 。
# 时间O(N),空间O(N) 遍历法,最容易想也是最简单的思路
def solution(head):
    visited = set()
    while head:
        if head in visited:
            return head
        visited.add(head)
        head = head.next
    return None

# 快慢指针
'''
假设链表长度为a+b,a是无环的长度,b是环的长度                          
根据：
f=2s （快指针每次2步，路程刚好2倍）
f = s + nb (相遇时，刚好多走了n圈）
推出：s = nb
从head结点走到入环点需要走 ： a + nb， 而slow已经走了nb，那么slow再走a步就是入环点了。
如何知道slow刚好走了a步？ 从head开始，和slow指针一起走，相遇时刚好就是a步
'''
# 基本思路，先判断环，再判断环的入口
def solution1(head):
    slow, fast = head, head
    while True:
        if not fast or not fast.next:
            return
        slow, fast = slow.next, fast.next.next
        # 说明有环
        if fast == slow:
            break
    # 求环的第一个节点,这个时候,slow肯定在环里面了,而fast指针走的路程是slow的两倍,当slow走到环口,fast也一定在,这是理论基础
    fast = head
    while fast != slow:
        slow, fast = slow.next, fast.next
    return fast



















