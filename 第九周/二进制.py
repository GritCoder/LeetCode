# 一些常见的基本操作
# 一个数跟0异或 结果是它本身
# print(5^0)
# 自己跟自己异或 结果是0
# print(5^5)
# 由上面两个推导出：a=a^b^b

# 移除最后一个 1  a=n&(n-1) 这个性质可以用来统计二进制中 1 的个数
# 获取最后一个 1  diff=(n&(n-1))^n 上面的理解了 这个性质就很简单了

# 几个例题
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# def func(nums):
#     if not nums:
#         return
#     ans = 0
#     for item in nums:
#         ans = ans ^ item
#     return ans
# print(func([3,1,1,2,2]))
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现三次。找出那个只出现了一次的元素。
# def solution1(nums):
#     if not nums:
#         return
#     hashSet = set(nums) # 这个方法类似的也可以求解出现两次的情况 很简单
#     return (3 * sum(hashSet) - sum(nums)) // 2
# 暴力法(通用)
# def solution2(nums):
#     if not nums:
#         return
#     dic = {} # 字符为key 次数为值的字典
#     for c in nums: # 若是统计字符最后出现的位置 可以用 for i, c in enumrate(nums): dic[c] = i
#         dic[c] = dic[c] + 1 if c in dic else 1 # 统计每个字符出现的次数
#     for x in dic.keys():
#         if dic[x] == 1:
#             return x
# print(solution2([1,1,1,2,2,2,3]))
# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
# 暴力大法好～
# def func(nums):
#     if not nums:
#         return
#     ans, dic =[], {}
#     for item in nums:
#         dic[item] = dic[item] + 1 if item in dic else 1
#     for item in dic.keys():
#         if dic[item] == 1:
#             ans.append(item)
#     return ans
# print(func([1,1,2,3,4,4]))
# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
# def func(num):
#     def cal(i):
#         tmp = 0
#         while i:
#             tmp += 1
#             i = i & (i-1)
#         return tmp
#     ans = [0] * (num + 1)
#     for i in range(num+1):
#         ans[i] = cal(i) # 一个数会求了 多个数也很简单 写个循环就好了
#     return ans
# print(func(5))
# 反转一个32位的无符号二进制串
# def func(bits):
#     ans, lens = 0, 31 # 注意初始化的是31 因为一开始有一位了
#     # Python可以自动处理 这些操作都会自动转换成对应的二进制去操作
#     while bits:
#         ans += (bits & 1) << lens # (bits & 1) 是提取最后一位  左移是因为反转 右面的要到左边来了
#         bits >>= 1 # 最右边那一位已经处理了 直接移位溢出就行
#         lens -= 1 # 处理完一位 长度减一
#     return ans
# print(func('00000010100101000001111010011100'))
# 区间按位与
# def func(m, n):
#     ans = m
#     for item in range(m+1, n+1):
#         ans = ans & item
#     return ans
# print(func(5, 7))
# 整数反转 可以用字符串的方式做 也可以用数学法来做 字符串比较简单 直接取反即可 下面是数学法 都要注意边界条件 注意正负数
def reverse(x):
    rev = 0
    if -2147483648 <= x <= 2147483647:
        tmp = abs(x)
        while tmp != 0:
            pop = tmp % 10 # 取最后一位
            tmp = tmp // 10 # 取整除
            rev = rev * 10 + pop # 新的数字
        if -2147483648 <= rev <= 2147483647: # 注意反转后的数也要判断一下 其他就没啥了～ 注意细节
            if x > 0:
                return rev
            else:
                return -rev
        else:
            return 0
    else:
        return 0 # 表示越界
print(reverse(-123))


