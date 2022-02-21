
class Curve:
    def __init__(self, A, gamma, D, n, p=None):
        self.A = A
        self.gamma = gamma
        self.n = n
        if p:
            self.p = p
        else:
            self.p = [10 ** 18] * n
        self.x = [D // n * 10**18 // self.p[i] for i in range(n)]

    def xp(self):
        return [x * p // 10 ** 18 for x, p in zip(self.x, self.p)]
