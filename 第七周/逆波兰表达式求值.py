# 碰到操作数入栈，碰到运算符将栈顶的两个元素弹出，并将计算结果入栈
# 注意 eval() 函数的应用，这个是求字符串表达式的一个函数
def solution(lis):
    stack = []
    for item in lis:
        if item in '+-*/':
            num1 = stack.pop()
            num2 = stack.pop()
            val = str(int(eval(num2+item+num1)))
            stack.append(val)
        else:
            stack.append(item)
    return int(stack[0])
print(solution(["2", "1", "+", "3", "*"]))