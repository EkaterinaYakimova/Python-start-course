a = [[51, 31, 13, 66], [44, 44, 47, 57]]
x = [[0, 1, 2, 3], [6, 78, 27, 26], [3, 8, 9, 0], [89, 78, 87, 209]]


class Matrix:

    def __init__(self, spisok):
        self.spisok = spisok

    def __str__(self):
        return '\n'.join(map(str, self.spisok))

    def __add__(self, other):
        c = []
        for i in range(len(self.spisok)):
            c.append([])
            for j in range(len(self.spisok[0])):
                c[i].append(self.spisok[i][j] + other.spisok[i][j])
        return '\n'.join(map(str, c))


mat1 = Matrix(a)
mat2 = Matrix(x)

print(mat1)
print(mat2)
print(mat1+mat2)