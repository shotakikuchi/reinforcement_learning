import numpy as np
from normal_dist_random import NormalDistRandom


class Bandit:
    def __init__(self, size=10, reward_exp_avg=0.0, reward_exp_var=1.0, reward_var=1.0):
        self.size = size
        self.rand_generator = [None] * self.size
        self.reward_exp = np.zeros(self.size)

        random = NormalDistRandom(reward_exp_avg, reward_exp_var)

        for i in range(size):
            reward_exp = random.get_random()
            print(reward_exp)
            self.reward_exp[i] = reward_exp
            self.rand_generator[i] = NormalDistRandom(reward_exp, reward_var)

    def select(i):
        return self.rand_generator[i].get_random()

