class Cell:

    def __init__(self, qty):
        self.qty = int(qty)

    def __add__(self, other):
        return self.qty + other.qty

    def __sub__(self, other):
        return self.qty - other.qty

    def __mul__(self, other):
        return self.qty * other.qty

    def __truediv__(self, other):
        return Cell(round(self.qty / other.qty))

    def make_order(self, nums):
        return '\n'.join(['*' * self.qty for _ in range(nums // self.qty)]) + '\n' + '*' * (nums % self.qty)

cell1 = Cell(1)
cell2 = Cell(2)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1.qty / cell2.qty)
print(cell1.make_order(10))
