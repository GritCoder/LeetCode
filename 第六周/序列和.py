'''
给出一个正整数N和长度L，找出一段长度大于等于L的连续非负整数，他们的和恰好为N。答案可能有多个，我们需要找出长度最小的那个。
例如 N = 18 L = 2：
5 + 6 + 7 = 18
3 + 4 + 5 + 6 = 18
都是满足要求的，但是我们输出更短的 5 6 7
从小到大输出这段连续非负整数，以空格分隔，行末无空格。
如果没有这样的序列或者找出的序列长度大于100，则输出No
'''
# 利用等差数列的思想，详细讲解见 https://www.nowcoder.com/questionTerminal/46eb436eb6564a62b9f972160e1699c9?commentTags=Python
def solution(N, L):
    flag = False
    for i in range(L, 101):
        a_start = (2*N-i**2+i) / (2*i) # 注意已经做了等价转换了
        if int(a_start) == a_start: # 因为Python3这个除自动是小数了
            flag = True
            a_start = int(a_start)
            for j in range(i-1): # 从输出来看，序列的长度取决于i的大小 因此第一个找到的就是最短的(后面就自增了)
                print(a_start+j, end=' ')
            print(a_start+i-1) # 注意，最后一位不要空格 要单独输出
            break
    if not flag:
        print('No')
solution(18, 2)