# 注意区分环路检测  这里只需要判断是否有环即可
def hasCycle(head):
    if not head or not head.next:
        return False
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
        if slow == fast:
            break
    if fast != slow: # 要判断  因为循环体不一定是从break那里跳出来的  也可能是循环体正常结束
        return False
    else:
        return True