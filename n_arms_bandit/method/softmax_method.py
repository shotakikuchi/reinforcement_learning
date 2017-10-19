# coding: utf-8
import numpy as np


class SoftmaxMethod:
    def __init__(self, size=10, temperature=0.1, stepsize=10):
        """

        :param size: n本腕バンディット問題のサイズ
        :param temperature: 温度（学習パラメータ）
        :param stepsize: ステップサイズ
        """
        self.size = size
        self.temperature = temperature
        self.stepsize = stepsize
        self.values = np.zeros(self.size)
        self.times = np.zeros(self.size)
        self.weights = np.ones(self.size)

    def select(self):
        """
        各腕の重みをexp(values[i]/temperature)とし、
        重みに従った確率で腕を選ぶ。
        --
        価値が高いほど、重みが大きくなるので選ばれやすい。
        ただし、温度が高い場合、重みは相対的に小さくなり、
        他の行動が選ばれる可能性も高くなる。

        :return:
        """

        weight_total = np.sum(self.weights)
        rand = np.random.rand() * weight_total
        selected = 0
        for i in range(self.size):
            if rand <= self.weights[i]:
                selected = i
                break
            else:
                rand -= self.weights[i]

        return selected

    def reflect(self, selected, value):
        """得られた報酬を反映し、学習する

        :param selected: 選んだ腕
        :param value: 得られた報酬
        :return:
        """
        self.times[selected] += 1
        stepsize = self.stepsize if self.stepsize else (1.0 / self.times[selected])
        self.values[selected] += stepsize * (value - self.values[selected])
        self.weights[selected] = np.exp(self.values[selected]/ self.temperature)



