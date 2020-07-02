'''
给定一个有环链表，实现一个算法返回环路的开头节点。
有环链表的定义：在链表中某个节点的next元素指向在它前面出现过的节点，则表明该链表存在环路。
思路:快慢指针
创建指针 fast 和 slow；
slow 每走一步， fast 走两步；
两者相遇时，将 slow 指针指向 head；
以同样的速度移动 fast 和 slow，再次相遇的结点即为所求结果。
'''
def detectCycle(head):
    slow, fast = head, head
    while fast and fast.next:  # 开始走位
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # 相遇
            break
    # 若无相会处，则无环路
    if not fast or not fast.next:
        return None
    # 若两者以相同的速度移动，则必然在环路起始处相遇
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
