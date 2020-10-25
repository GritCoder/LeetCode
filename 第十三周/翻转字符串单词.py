# 利用API
def solution1(s):
    ans = s.split()
    ans = ans[::-1]
    return ' '.join(ans)

# 双端队列，从头部插入，就已经实现逆序了
import collections
def solution2(s):
    left, right = 0, len(s) - 1
    # 去掉字符串开头的空白字符
    while left <= right and s[left] == ' ':
        left += 1
    # 去掉字符串结尾的空白字符
    while left <= right and s[right] == ' ':
        right -= 1
    queue, word = collections.deque(), []
    # 循环里面不需要考虑字符串结尾是否分割添加正确，因为当到最后时候，while循环已经跳出了
    while left <= right:
        # 是一个字符一个字符添加的，如果遇到空格了，说明这个单词结束了，就放进队列中
        if s[left] == ' ' and word:
            queue.appendleft(''.join(word))
            word = []
        # 当单词还没有结束时，继续把字符放进word中
        elif s[left] != ' ':
            word.append(s[left])
        # 指针后移，处理下一个字符
        left += 1
    # 循环结束的时候，最后一个单词还没有添加进去，在这里添加
    queue.appendleft(''.join(word))
    # print(queue)
    # 最后用空格连接，并返回结果
    return ' '.join(queue)
print(solution2('hello world!'))