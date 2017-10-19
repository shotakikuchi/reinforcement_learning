# coding: utf-8

import numpy as np


class TestRuner:
    """n本腕バンディット問題について、
        特定のアルゴリズムを使って
        指定された回数の試行を行うクラス
    """

    def __init__(self, bandit, method):
        """

        :param bandit:
        :param method:
        """
        self.bandit = bandit
        self.method = method
        self.count = 0
        self.total_reward = 0

    def execute(self, count):
        """指定された回数、試行を行う。

        :return:
        """
        for i in range(count):
            selected_arm = self.method.select()
            reward = self.bandit.select(selected_arm)
            self.total_reward += reward
            self.method.reflect(selected_arm, reward)
        self.count += count

    def average(self):
        """得られた報酬の平均を返す。

        :return:
        """
        return (self.total_reward * 1.0) / self.count or 0.0

    def max_exp(self):
        """報酬の期待値の最大値を返す。

        :return:
        """
        return np.max(self.bandit.reward_exp)

    def optimality(self):
        return self.average() / self.max_exp()


if __name__ == "__main__":
    from bandit import Bandit
    from n_arms_bandit.method.greedy_method import GreedyMethod

    size = 10

    bandit = Bandit(size=size)
    greedy = TestRuner(bandit=bandit, method=GreedyMethod(size=size))

    epsilon_greedy = TestRuner(bandit=bandit, method=GreedyMethod(size=size, epsilon=0.1))

    for runner in [greedy, epsilon_greedy]:

        print(
            """
-------------------------------
time  reward avg.  optimality
-------------------------------
"""
        )

        for i in range(20):
            runner.execute(100)
            print("selected arm : {}".format(runner.method.select()))
            print("{} {} {}".format(runner.count, runner.average(), runner.optimality()))
