# 自己的解法，其实就是用的count来做的，但提交时超时了
# class WordsFrequency:
#     def __init__(self, book):
#         self.book = book
#         self.dic = {}
#         for word in self.book:
#             self.dic[word] = self.book.count(word)
#     def get(self, word: str) -> int:
#         if word in self.dic.keys():
#
#             return self.dic[word]
#         else:
#             return 0

# 其他解法
class WordsFrequency:
    def __init__(self, book):
        self.book = book
        self.dic = {}
        for word in self.book:
            # 这个计数方式比count高效
            self.dic[word] = 1 if word not in self.dic.keys() else self.dic[word] + 1
    def get(self, word: str) -> int:
        if word in self.dic.keys():
            return self.dic[word]
        else:
            return 0

# 总结一下 碰见计数相关的 常见的有两种方法，一是直接调用count，一是利用字典来搞 见22行代码