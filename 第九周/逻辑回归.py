import numpy as np
# 代码不可运行 贵在熟悉思路
class LR(object):
    def __init__(self):
        pass
    # 定义激活函数
    def sigmoid(x):
        return 1.0 / (1 + np.exp(-x))
    # 类似地...
    def Relu(x):
        return x if x >= 0 else 0
    # 定义损失函数
    def error(pre, label):
        errorSum = 0.0
        # batchsize
        m = np.shape(pre)[0]
        for i in range(m):
            if pre[i] > 0 and 1 - pre[i] > 0:
                errorSum += (-label[i] * np.log(pre[i]) - (1 - label[i]) * np.log(1-pre[i]))
                # errorSum -= label[i] * np.log(pre[i]) + (1 - label[i]) * np.log(1 - pre[i])
            else:
                errorSum += 0.0
        return errorSum / m
    # 梯度下降优化参数
    def SGD(alpha, label, maxIteration, feature):
        w = np.mat
        i = 0
        while i <= maxIteration:
            i += 1
            sig = sigmoid(feature * w)
            err = label - sig
            w = w + alpha * feature.T * err # 权重修正
        return w

    # 加载数据集
    # 加载权重

    # 预测函数
    def predict(feature, w):
        sig = sigmoid(feature * w.T)
        m = np.shape(sig)[0]
        for i in range(m):
            if sig[i] < 0.5:
                sig[i] = 0.0
            else:
                sig[i] = 1.0
        return sig

