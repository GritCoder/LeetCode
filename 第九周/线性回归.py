import numpy as np
class linear(object):
    def __init__(self):
        self.W = None
        self.b = None

    def loss(self, X, y):
        num_feature = X.shape[1]
        num_train = X.shape[0]

        h = X.dot(self.W) + self.b
        loss = 0.5 * np.sum(np.square(h - y)) / num_train

        dW = X.T.dot((h - y)) / num_train
        db = np.sum((h - y)) / num_train

        return loss, dW, db

    def train(self, X, y, learn_rate=0.001, iters=10000):
        num_feature = X.shape[1]
        self.W = np.zeros((num_feature, 1))
        self.b = 0
        loss_list = []

        for i in range(iters):
            loss, dW, db = self.loss(X, y)
            loss_list.append(loss)
            self.W += -learn_rate * dW
            self.b += -learn_rate * db

            if i % 500 == 0:
                print
                'iters = %d,loss = %f' % (i, loss)
        return loss_list

    def predict(self, X_test):
        y_pred = X.dot(self.W) + self.b
        return y_pred

    pass
