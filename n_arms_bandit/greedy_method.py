# coding: utf-8
import numpy as np


class GreedyMethod:
    """Greedy Method
    """

    def __init__(self, size=10, epsilon=0.0, stepsize=10):
        self.size = size
        self.epsilon = epsilon
        self.stepsize = stepsize
        self.times = np.zeros(self.size)
        self.values = np.zeros(self.size)

    def select(self):
        """グリーディ法で腕を選ぶ
           epsilonの確率で、ランダムに選択を行う。
           そうでない場合、最も価値が高いと推定される行動を選ぶ。
        """
        if np.random.random() < self.epsilon:
            return np.random.rand()
        else:
            max_value = np.max(self.values)
            return self.values.index(max_value)

    def reflect(self, selected, value):
        """得られた報酬を反映し、学習する。
        :params selected: 選んだ腕
        :params value: 得られた報酬
        """
        self.times[selected] += 1
        stepsize = self.stepsize if self.stepsize else (1.0 / self.times[selected])
        self.values[selected] += stepsize * (value - self.values[selected])
