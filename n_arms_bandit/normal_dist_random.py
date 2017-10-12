# coding: utf-8
import numpy as np

np.random.seed(111)


class NormalDistRandom:
    """正規分布に従った乱数を生成するクラス
    """

    def __init__(self, exp=0.0, var=1.0):
        """期待値exp, 分散varの正規分布に従った乱数を生成する乱数生成器を作成する。
        """
        self.exp = exp
        self.var = var
        self.values = []

    def get_random(self):
        if len(self.values) == 0:
            # ボックス＝ミュラー法で乱数を生成する

            # np.random.random()は[0, 1)で値を返すので、
            # (0, 1]に変換する。
            a = 1.0 - np.random.random()
            b = 1.0 - np.random.random()

            z1 = np.sqrt(-2.0 * np.log(a)) * np.cos(2 * np.pi * b)
            z2 = np.sqrt(-2.0 * np.log(a)) * np.sin(2 * np.pi * b)

            rand1 = z1 * np.sqrt(self.var) + self.exp
            rand2 = z2 * np.sqrt(self.var) + self.exp

            self.values += [rand1, rand2]
        return self.values.pop(0)
