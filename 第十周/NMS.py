import numpy as np
# 注意一点，相关操作都是numpy矩阵操作，不要从list的角度去理解代码
def NMS(dets, th):
    # 输入参数为候选框的列表 阈值
    x1 = dets[:, 0] # 这种切片方式要习惯，意思是行全取，列取索引为 0 的
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    scores = dets[:, 4]
    # 计算每一个候选框的面积
    areas = (x2-x1+1) * (y2-y1+1)
    # 根据得分排序
    order = np.argsort(scores)[::-1] # 返回的是scores中从小到大的索引值, 逆序切片后就变成从大到小了
    keep = [] # 最终要保留的box
    while order.size > 0:
        i = order[0] # 因为是从大到小排序的，一开始取得分最大的box
        keep.append(i)
        # 计算当前得分最大框与其他框的相交坐标，会用到numpy的broadcast机制，得到的是向量
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.maximum(x2[i], x2[order[1:]])
        yy2 = np.maximum(y2[i], y2[order[1:]])
        # 计算相交框的宽和高，不可能为负，所以跟0比，得到的仍然是向量
        w, h = np.maximum(0.0, xx2-xx1+1), np.maximum(0.0, yy2-yy1+1)
        inter = w * h
        # 计算IOU 重叠面积/(面积1+面积2-重叠面积)
        iou = inter / (areas[i]+areas[order[1:]]-inter)
        # 找到iou小于th阈值的box，保留下来 # np.where()[0] 表示行的索引, np.where()[1] 则表示列的索引
        inds = np.where(iou <= th)[0] # np.where实际上返回的是坐标，并且可作为索引去再找出矩阵a的对应值
        # 将order序列更新，由于前面得到的矩形框索引要比矩形框在原order序列中的索引小1，所以要把这个1加回来
        # 为什么会小 1 呢， 是因为一开始你从order里面把得分最大的取出来了，去计算剩余的 n-1 个box的iou
        # 因此得到的结果索引是相对于 n-1 的，而你现在要更新的order是相对于原始的，因此减去 1
        order = order[inds+1]
    return keep
# test
if __name__ == "__main__":
    dets = np.array([[30, 20, 230, 200, 1],
                     [50, 50, 260, 220, 0.9],
                     [210, 30, 420, 5, 0.8],
                     [430, 280, 460, 360, 0.7]])
    thresh = 0.35
    keep_dets = NMS(dets, thresh)
    print(keep_dets)
    print(dets[keep_dets])



