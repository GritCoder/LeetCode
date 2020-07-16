# 其实很简单 字典按 key 或者 value 进行排序 面试问到了 记录一下
def solution(dic):
    print(dic)
    # res = sorted(dic) # 如果不指定key参数，字典排序默认的是对 键 进行排序
    # key 必须是一个映射 或者说是一个函数  具体还可以参考 第四周 把数组数排列成最小 那个程序
    res = sorted(dic.items(), key=lambda item: item[1])
    # lambda里面可以指定多个排序规则 如果第一项一样 则按第二个来比较 等等
    # res = sorted(dic.items(), key=lambda item:(item[1][0],item[1][-1])) # 按 值 进行排序
    print(res) # 结果是一个元组的列表
solution({'xiaoming': 100, 'li': 10, 'shi':200})
# solution({'xiaoming': [100,30], 'li': [180,10], 'shi':[100,200]})