# 注意区分环路检测  这里只需要判断是否有环即可
def hasCycle(head):
    if not head or not head.next:
        return False
    slow, fast = head, head.next
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True