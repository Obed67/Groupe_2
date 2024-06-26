from typing import List, Tuple, Union


class Array:
    def __init__(self, data: Union[List[int], List[List[int]]]):
        # Initialisation de l'Array avec les données fournies
        self.data = data
        if isinstance(data[0], list):
            # Déterminer la forme (shape) pour un tableau 2D
            self.shape = (len(data), len(data[0]))
        else:
            # Déterminer la forme (shape) pour un tableau 1D
            self.shape = (len(data),)

    def __add__(self, other: Union[int, 'Array']) -> 'Array':
        if isinstance(other, int):
            # Addition avec un scalaire
            return Array([[item + other for item in row] for row in self.data]) if self.is_2d() else Array(
                [item + other for item in self.data])
        else:
            if self.shape != other.shape:
                raise ValueError("Shapes do not match for addition")
            # Addition élément par élément pour des tableaux de même forme
            return Array([[self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))] for i in
                          range(len(self.data))]) if self.is_2d() else Array(
                [self.data[i] + other.data[i] for i in range(len(self.data))])

    def __sub__(self, other: Union[int, 'Array']) -> 'Array':
        if isinstance(other, int):
            # Soustraction avec un scalaire
            return Array([[item - other for item in row] for row in self.data]) if self.is_2d() else Array(
                [item - other for item in self.data])
        else:
            if self.shape != other.shape:
                raise ValueError("Shapes do not match for subtraction")
            # Soustraction élément par élément pour des tableaux de même forme
            return Array([[self.data[i][j] - other.data[i][j] for j in range(len(self.data[0]))] for i in
                          range(len(self.data))]) if self.is_2d() else Array(
                [self.data[i] - other.data[i] for i in range(len(self.data))])

    def __mul__(self, other: Union[int, 'Array']) -> 'Array':
        if isinstance(other, int):
            # Multiplication avec un scalaire
            return Array([[item * other for item in row] for row in self.data]) if self.is_2d() else Array(
                [item * other for item in self.data])
        else:
            if self.shape != other.shape:
                raise ValueError("Shapes do not match for multiplication")
            # Multiplication élément par élément pour des tableaux de même forme
            return Array([[self.data[i][j] * other.data[i][j] for j in range(len(self.data[0]))] for i in
                          range(len(self.data))]) if self.is_2d() else Array(
                [self.data[i] * other.data[i] for i in range(len(self.data))])

    def __truediv__(self, other: Union[int, 'Array']) -> 'Array':
        if isinstance(other, int):
            # Division avec un scalaire
            return Array([[item / other for item in row] for row in self.data]) if self.is_2d() else Array(
                [item / other for item in self.data])
        else:
            if self.shape != other.shape:
                raise ValueError("Shapes do not match for division")
            # Division élément par élément pour des tableaux de même forme
            return Array([[self.data[i][j] / other.data[i][j] for j in range(len(self.data[0]))] for i in
                          range(len(self.data))]) if self.is_2d() else Array(
                [self.data[i] / other.data[i] for i in range(len(self.data))])

    def __matmul__(self, other: 'Array') -> int:
        if len(self.shape) != 1 or len(other.shape) != 1:
            raise ValueError("Dot product only supports 1D arrays")
        if self.shape != other.shape:
            raise ValueError("Shapes do not match for dot product")
        # Produit scalaire de deux tableaux 1D
        return sum(self.data[i] * other.data[i] for i in range(len(self.data)))

    def __contains__(self, item: int) -> bool:
        # Recherche d'un élément
        if self.is_2d():
            return any(item in row for row in self.data)
        else:
            return item in self.data

    def __getitem__(self, key: Union[int, Tuple[int, int], slice]) -> Union[int, List[int]]:
        # Indexage et slicing
        if isinstance(key, tuple):
            return self.data[key[0]][key[1]]
        return self.data[key]

    def __len__(self) -> int:
        # Longueur du tableau (nombre d'éléments en 1D, nombre de lignes en 2D)
        return len(self.data)

    def is_2d(self) -> bool:
        # Vérifie si le tableau est 2D
        return isinstance(self.data[0], list)

    def __repr__(self) -> str:
        # Représentation de l'objet Array
        return f'Array({self.data})'


# Exemple d'utilisation
a = Array([1, 2, 3, 4])
b = Array([4, 3, 2, 1])
c = Array([[1, 2], [3, 4]])
d = Array([[4, 3], [2, 1]])

print(a + b)  # Array([5, 5, 5, 5])
print(c + d)  # Array([[5, 5], [5, 5]])
print(a * 2)  # Array([2, 4, 6, 8])
print(c * 2)  # Array([[2, 4], [6, 8]])
print(a @ b)  # 20
print(3 in a)  # True
print(c[1, 0])  # 3
print(a[1:3])  # [2, 3]
var = a.shape
print(var)
