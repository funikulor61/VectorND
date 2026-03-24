import math     #импортим

class Vector_nd():          #создаем класс
    def __init__(self, *args):      #конструктор
        self._cords = list(args)

    def __str__(self):          #обозначение функции для выдачи имени обьекта
        return f"Vector{tuple(self._cords)}"
    
    def __add__(self, other):           #функция сложения двух векторов
        result = []
        for i in range(len(self._cords)):
            sum1 = self._cords[i] + other._cords[i]
            result.append(sum1)
        return Vector_nd(*result)
    
    def __mul__(self, num):              #функция умножения вектора на число
        result = []
        for i in range(len(self._cords)):
            multiplicat = self._cords[i] * num
            result.append(multiplicat)
        return Vector_nd(*result)
    
    def __rmul__(self, num):                #функция умножения числа на вектор
        result = []
        for i in range(len(self._cords)):
            multiplicat = num * self._cords[i] 
            result.append(multiplicat)
        return Vector_nd(*result)
    
    def __sub__(self, other):           #функция разности двух векторов
        result = []
        for i in range(len(self._cords)):
            sum2= self._cords[i] - other._cords[i]
            result.append(sum2)
        return Vector_nd(*result)
    
    def __truediv__(self, num):     #функция деления вектора на число
        result = []
        for i in range(len(self._cords)):
            division = self._cords[i] / num
            result.append(division)
        return Vector_nd(*result)
    
    def __neg__(self):              #функция инверсии
        result = []
        for i in range(len(self._cords)):
            multiplicat = self._cords[i] * -1
            result.append(multiplicat)
        return Vector_nd(*result)
    
    def __abs__(self):              #функция нахождения длины вектора
        sum3 = 0
        for i in range(len(self._cords)):
            sum3 += self._cords[i] ** 2
        return sum3 ** 0.5

    def __eq__(self, other):                #функция сравнения векторов
        return self._cords == other._cords
    
    def __len__(self):              #функция размерности
        return len(self._cords)
    
    def __getitem__(self, ind):         #функция для обращения элементов и срезов
        return self._cords[ind]
    
    def __iter__(self):             # Возвращаем готовый итератор внутреннего списка
        return iter(self._cords)
    
    def dot(self, other):               #функция скалярного произведения
        if len(self) != len(other):
            print("Разные размеры векторов")
        else:
            sp = []
            for i in range(len(self)):
                sp.append(self._cords[i] * other._cords[i])
            return Vector_nd(sp)
    
    def hash(self):                             #функция хэширования
        st = " ".join(str(x) for x in self._cords) 
        return hash(st)
    
    def norm(self):             #функция для нормализованного(единичного) вектора
        spis = ()
        spis += (-1 * self._cords[1], self._cords[0], )
        for i in range(2, len(self._cords)):
            spis += (0, )
        return Vector_nd(spis)



"""
v = Vector_nd([10, 20, 30])
for x in v:
    print(x)



v1 = Vector_nd(1, 2, 3, 4, 5, 6)

v5 = Vector_nd(1,2,3,4,5,6)
v7 = Vector_nd(2,3,4,5,6,6)


a = v1.hash()
b = v5.hash()
c = v7.hash()
print(a)
print(set([a, b ,c]))

v11 = v1 + v5
v12 = v1 - v5
print(v11, v12)

v2 = v1.__neg__()
print(v2)

v3 = v1.__abs__()
print(v3)

v4 = v1 / 0.5
print(v4)

v6 = v1.__len__()
print(v6)

print(v1 == v5)

print(v1[1:3])
print(v1[0])

print(v1.dot(v5))

print(v1.norm())


"""