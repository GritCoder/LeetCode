# 数组去重
# 主要考虑三个条件，第一，去重；第二，不能打乱s中的相对顺序；第三，若有多个结果，返回字典序最小的那个
# 下面没有注释的代码满足第一和第二，若要满足第三点，把代码去掉注释即可
# 当有多个条件时，各个击破，一个一个来考虑
def solution1(s):
    ans = []
    # flag为标记，存放已经添加的元素
    flag = set()
    # cnt = {}
    # 维护一个字符的计数器
    # for c in s:
    #     cnt[c] = 1 if c not in cnt else cnt[c] + 1
    # print(cnt)
    for c in s:
        # 每个元素访问之后，次数减1
        # cnt[c] -= 1
        if c in flag:
            continue
        # while ans and ans[-1] > c:
        # 如果这个元素的次数为0了，说明后面没有了，则不能删除
        #     if cnt[ans[-1]] == 0:
        #         break
        #     flag.remove(ans.pop())
        ans.append(c)
        flag.add(c)
    print(''.join(ans))
# solution1("ecbacba")

# 有序数组原地去重 O(1)空间复杂度 快慢指针
def solution2(arrs):
    n = len(arrs)
    if n == 0:
        return 0
    slow, fast = 0, 1
    # nums = []
    while fast < n:
        if arrs[fast] != arrs[slow]:
            slow += 1
            # 维护 0...slow 无重复
            arrs[slow] = arrs[fast]
            # print(arrs)
            # nums.append(arrs[fast])

        fast += 1
    # 返回无重复数组的长度或者无重复数组都可以，具体看题目要求
    return slow + 1, arrs[:slow+1]
# print(solution2([1,1,2,2,2,3]))

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 有序链表去重 仍然是快慢指针
def solution3(head):
    if not head:
        return
    slow, fast = head, head.next
    while fast:
        if fast.val != slow.val:
            # arrs[slow] = arrs[fast]
            slow.next = fast
            # slow++
            slow = slow.next
        # fast++
        fast = fast.next
    # 断开与后面重复元素的连接
    slow.next = None
    return head

# 无序链表去重
def solution4(head):
    if not head:
        return head
    dummy = ListNode(0)
    dummy.next = head
    cur = head
    while cur:
        while cur.next and cur.val == cur.next.val:
            cur.next = cur.next.next
        cur = cur.next
    return dummy.next

# 然后无序数组去重的话，可以转换成字符串，然后再去重，这样就跟字符串去重代码一样了
pass