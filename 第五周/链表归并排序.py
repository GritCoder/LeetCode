class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def createList(self, data):
        head = ListNode(data[0])
        p = head
        for i in range(1, len(data)):
            node = ListNode(data[i])
            p.next = node
            p = p.next
        return head


def sortList(head):
    def merge(left, right):
        h = ListNode(0)
        res = h
        while left and right:
            if left.val < right.val:
                res.next = left
                left = left.next
            else:
                res.next = right
                right = right.next
            res = res.next
        res.next = left if left else right  # 连接剩余的部分(如果有)
        return h.next  # 因为res是哑结点
    def recursion(head):
        slow, fast = head, head.next
        while fast and fast.next:  # 快指针走两步 其到达终点时慢指针正好到中间
            fast = fast.next.next
            slow = slow.next
        return slow

    if not head or not head.next: return head
    mid = recursion(head)
    tail = mid.next # 这句话必须加 不加会导致前半部分跟后半部分断链 导致死循环 其实就是中间变量
    mid.next = None # 等于None表示切断前半部分去做递归 但不是完全意义上的切断 还需要用tail连接
    left = sortList(head)
    # right = sortList(mid)
    right = sortList(tail) # 也不能直接传入mid.next 因为前面其已经设置为 None 需要引入中间变量
    res = merge(left, right)
    return res

obj = ListNode(0)
lis = obj.createList([4,2,1,3])

res = sortList(lis)
while res:
    print(res.val)
    res = res.next