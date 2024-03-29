import random
import time


class Percolate:
    def __init__(self, side):
        self._side = side
        self._square = side**2
        self._parents = list(range(self._square + 2))
        self._closed = set(range(self._square))
        self._size = [1] * (self._square + 2)

    def frac_open(self):
        return 1-len(self._closed) / self._square

    def open(self, choice):
        if choice not in self._closed:
            return
        self._closed.remove(choice)
        for direction in (-self._side, -1, 1, self._side):
            new_pos = choice + direction
            if new_pos < 0:
                new_pos = self._square
            elif new_pos >= self._square:
                new_pos = self._square + 1
            if new_pos not in self._closed:
                self._union(choice, new_pos)

    def _union(self, p, q):
        i = self._root(p)
        j = self._root(q)
        if i == j:
            return
        if self._size[i] < self._size[j]:
            self._parents[i] = j
            self._size[j] += i
        else:
            self._parents[j] = i
            self._size[i] += j

    def _root(self, n):
        while self._parents[n] != n:
            self._parents[n] = self._parents[self._parents[n]]
            n = self._parents[n]
        return n

    def connected(self, p, q):
        return self._root(p) == self._root(q)

    def percolates(self):
        return self.connected(self._square, self._square+1)


if __name__ == "__main__":
    sides = [10, 20, 40, 80, 160, 320, 640, 1280, 2560]
    for side in sides:
        coeffs = []
        for i in range(20):
            entries = list(range(side**2))
            random.shuffle(entries)
            perc = Percolate(side)
            t_total = 0
            now = time.time()
            while not perc.percolates():
                perc.open(entries.pop())
            coeffs.append(perc.frac_open())
            done = time.time()
            t_total += done - now
        print(f"Size: {side} Time: {t_total:.3} s Value: {sum(coeffs)/len(coeffs):.4}")
