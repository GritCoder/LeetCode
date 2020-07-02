# leetcode代码
def getCommonNode(headA, headB):
    node1, node2 = headA, headB
    while node1 != node2:
        node1 = node1.next if node1 else headB # 核心代码，理解含义
        node2 = node2.next if node2 else headA
    return node1 # 最后返回node1和node2都是一样的，因为已经相遇了