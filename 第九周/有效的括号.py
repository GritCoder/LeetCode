'''
初始化栈 S。
一次处理表达式的每个括号。
如果遇到开括号，我们只需将其推到栈上即可。这意味着我们将稍后处理它，让我们简单地转到前面的 子表达式。
如果我们遇到一个闭括号，那么我们检查栈顶的元素。如果栈顶的元素是一个 相同类型的 左括号，那么我们将它从栈中弹出并继续处理。否则，这意味着表达式无效。
如果到最后我们剩下的栈中仍然有元素，那么这意味着表达式无效。
'''
def solution(s):
    stack = []
    dic = {")": "(", "}": "{", "]": "["}
    for c in s:
        # 右括号作为字典的key 左括号为值 注意初始化技巧
        if c in dic:
            top = stack.pop() if stack else '#'
            if dic[c] != top:
                return False
        else: # 左括号入栈
            stack.append(c)
    return not stack