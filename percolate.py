import random
import time

class Percolate:
    def __init__(self, side):
        self._side = side
        self._square = side**2
        self._parents = list(range(self._square+2))
        self._open = [False]*(self._square+2)
        self._open[-1] = True  # "top"
        self._open[-2] = True  # "bottom"
        self._size = [1]*(self._square+2)

    def frac_open(self):
        return 1-(sum(self._open)-2)/(len(self._parents)-2)
        
    def open(self, choice):
        if self._open[choice]:
            return
        self._open[choice] = True
        for direction in (-self._side, -1, 1, self._side):
            new_pos = choice + direction
            if new_pos < 0:
                new_pos = -2
            elif new_pos >= self._square:
                new_pos = -1
            if self._open[new_pos]:
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
        return self.connected(-2, -1)


if __name__ == "__main__":
    coeffs = []
    sides = [10, 20, 40, 80, 160, 320]
    for side in sides:
        now = time.time()
        for i in range(100):
            perc = Percolate(side)
            while not perc.percolates():
                perc.open(random.randint(0, side**2-1))
                coeffs.append(perc.frac_open())
        done = time.time()
        print(f"Size: {side} Time: {done-now:.2} s Value: {sum(coeffs)/len(coeffs)}")
            
