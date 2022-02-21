class Curve:

    """
    Python model of Curve pool math.
    """

    def __init__(self, A, D, n, p=None, tokens=None):
        """
        A: Amplification coefficient
        D: Total deposit size
        n: number of currencies
        p: target prices
        """
        self.A = A  # actually A * n ** (n - 1) because it's an invariant
        self.n = n
        self.fee = 10 ** 7
        if p:
            self.p = p
        else:
            self.p = [10 ** 18] * n
        if isinstance(D, list):
            self.x = D
        else:
            self.x = [D // n * 10 ** 18 // _p for _p in self.p]
        self.tokens = tokens

    def xp(self):
        return [x * p // 10 ** 18 for x, p in zip(self.x, self.p)]
