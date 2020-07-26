'''
基本思路：
1、遇到数字，转化为倍数
2、遇到 '['，将倍数和上次的结果入栈，倍数在本次计算的时候要用到，上次结果在本次计算完拼接字符串的时候需要用到
3、遇到 ']'，说明计算体已经结束了，可以进行计算和拼接结果了
4、遇到字符的话，直接拼接就行
本质上这个题跟逆波兰表达式有点类似，都是遇到不同的运算符或者特殊符号就进行处理，异曲同工。
'''
def solution(s):
    # init
    stack = []
    mul, res = 0, ""
    for item in s:
        if item == '[':
            stack.append([mul, res]) # 保存倍数和上一次的结果 下面会用到
            mul, res = 0, "" # 处理一次后要置空 不然就会影响后面的处理结果了
        elif item == ']':
            cur_mul, last_res = stack.pop()
            res = last_res + cur_mul * res
        elif '0' <= item <= '9':
            # 必须有 mul * 10 不然当遇到类似于 '13[a]' 这样的输入会导致结果求解错误
            mul = mul * 10 + int(item) # 字符转整型 乘10是进位的意思 比如你"123" item一开始指向1 下一次处理时要把这个数乘以10再加上当前的 才是对应的整型数值
        else:
            res += item
    return res
print(solution('3[a]2[bc]'))
# print(3 * 'a')
