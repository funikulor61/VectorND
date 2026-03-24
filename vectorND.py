import math

class Vector_nd():
    def __init__(self, *args):
        self._cords = list(args)

    def __str__(self):
        return f"Vector{tuple(self._cords)}"
    
    def __add__(self, other):
        result = []
        for i in range(len(self._cords)):
            sum = self._cords[i] + other._cords
            result.append(sum)
        return Vector_nd(*result)
    
    def __mul__(self, number):
        result = []
        for i in range(len(self._cords)):
            multiplicat = self._cords[i] * number
            result.append(multiplicat)
        return Vector_nd(*result)
    
    def __rmul__(self, number):
        result = []
        for i in range(len(self._cords)):
            multiplicat = number * self._cords[i] 
            result.append(multiplicat)
        return Vector_nd(*result)
    
    def __sub__(self, other):
        result = []
        for i in range(len(self._cords)):
            sum = self._cords[i] - other._cords
            result.append(sum)
        return Vector_nd(*result)
    
    def length(self):
        # Сумма квадратов всех координат
        sum_sq = 0
        for i in range(len(self.coords)):
            sum_sq += self.coords[i] ** 2
        
        # Квадратный корень (возведение в степень 0.5)
        return sum_sq ** 0.5
    
v1 = Vector_nd(1, 2, 3, 4, 5, 6)
v4 = v1 * 5
print(v4)