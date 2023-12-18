import matplotlib.pyplot as plt


class Point:

    def __init__(self, x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self.x = x
            self.y = y
        else:
            raise ValueError("Координаты могут быть только числами")


########################################################################################################################
class Section:

    def __init__(self, p1, p2):
        if not isinstance(p1, Point) or not isinstance(p2, Point):
            raise TypeError("Класс отрезок аргументами принимает только точки")
        self.x1 = p1.x
        self.y1 = p1.y
        self.x2 = p2.x
        self.y2 = p2.y
        self.len = self.lenght()
        if self.len == 0:
            raise ValueError("Длина отрезка не может быть равна 0")

    def lenght(self):
        return round((((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5), 2)

    def __eq__(self, other):
        return self.len == other.len

    def __lt__(self, other):
        return self.len < other.len

    # уравнение прямой y = k*x = b. Сначала ищем к, потом свободные переменные b.
    # и составляем систему уравнений для поиска точки пересечения прямых
    def cross(self, other):
        if self.x1 == self.x2:  # прямая параллельна оси ординат(x=x1)
            z1 = min(other.y1, other.y2)
            z2 = max(other.y1, other.y2)
            if min(self.y1, self.y2) < z1 < max(self.y1, self.y2) or min(self.y1, self.y2) < z2 < max(self.y1,
                                                                                                      self.y2):
                print(
                    "Отрезки лежат на одной прямой и имеют множество точек пересечения(т.е. накладываются друг на "
                    "друга)")
                return True
            elif z1 == max(self.y1, self.y2):
                print("Отрезки лежат на одной прямой и пересекаются в точке", "({},{})".format(self.x1, z1))
                return True
            elif z2 == min(self.y1, self.y2):
                print("Отрезки лежат на одной прямой и пересекаются в точке", "({}, {}".format(self.x1, z2))
                return True
            else:
                print("Отрезки лежат на одной прямой и не пересекаются")
                return False
        else:
            if self.y1 == self.y2:  # прямая параллельна оси абсцисс (k1=0)
                k1 = 0
                b1 = self.y1
            else:
                k1 = (self.y2 - self.y1) / (self.x2 - self.x1)
                b1 = self.y1 - k1 * self.x1
            if other.y1 == other.y2:
                k2 = 0
                b2 = other.y2
            else:
                k2 = (other.y2 - other.y1) / (other.x2 - other.x1)
                b2 = other.y1 - k2 * other.x1
            if k1 == k2:
                if b1 != b2:
                    print("Прямые параллельны, отрезки не пересекаются")
                    return False
                else:  # прямые совпадают
                    z1 = min(other.x1, other.x2)
                    z2 = max(other.x1, other.x2)
                    if min(self.x1, self.x2) < z1 < max(self.x1, self.x2) or min(self.x1, self.x2) < z2 < max(self.x1,
                                                                                                              self.x2):
                        print(
                            "Отрезки лежат на одной прямой и имеют множество точек пересечения(т.е. накладываются друг на "
                            "друга)")
                        return True
                    elif z1 == max(self.x1, self.x2):
                        y1 = k1 * z1 + b1
                        print("Отрезки лежат на одной прямой и пересекаются в точке", "({},{})".format(z1, y1))
                        return True
                    elif z2 == min(self.x1, self.x2):
                        y1 = k1 * z2 + b1
                        print("Отрезки лежат на одной прямой и пересекаются в точке", "({}, {}".format(z2, y1))
                        return True
                    else:
                        print("Отрезки лежат на одной прямой и не пересекаются")
                        return False
            # k1*x + b1 = k2*x + b2 - ищем точку пересечения прямых
            else:
                if k1 != k2:
                    x = round((b2 - b1) / (k1 - k2), 2)
                    y = round(k1 * x + b1, 2)
                    print("точка пресечения прямых", "({},{})".format(x, y))
                if min(self.x1, self.x2) <= x < max(self.x1, self.x2) and min(other.x1, other.x2) <= x <= max(other.x1,
                                                                                                              other.x2):
                    print("точка пресечения отрезков", "({},{})".format(x, y))
                    return True
                else:
                    print("Отрезки не пересекаются")
                    return False

    def draw(self, other):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        fig.set(facecolor="violet")
        ax.set(facecolor="pink")
        ax.set_xlim([-5, 10])
        ax.set_ylim([-5, 10])
        ax.set_title("Пересечение отрезков")
        ax.title.set_color("blue")
        ax.title.set_size(18)
        ax.set_xlabel("Ось абcцисс")
        ax.set_ylabel("Ось ординат")
        ax.plot([self.x1, self.x2], [self.y1, self.y2])
        ax.plot([other.x1, other.x2], [other.y1, other.y2], color='green')
        ax.scatter([self.x1, self.x2], [self.y1, self.y2])
        ax.scatter([other.x1, other.x2], [other.y1, other.y2], color='green')
        plt.show()


# # print("! Проверка ввода данных")
# # p1 = Point('2', -2)
# # p1 = Section(0, 9)
# # p1 = Point(0, -2)
# # p2 = Point(0, -2)
#
#
print("! Пример: Прямые параллельны и отрезки не пересекаются")
p1 = Point(0, -2)
p2 = Point(3, -2)
p3 = Point(1, 2)
p4 = Point(-1, 2)
s1 = Section(p1, p2)
s2 = Section(p3, p4)
print(s1 == s2, "Равенство длин отрезков")
print(s1 < s2, "Сравнение длин отрезков - первый короче второго")
print(s1 > s2, "Сравнение длин отрезков - первый длиннее второго")
print(s1.cross(s2))
s1.draw(s2)

print("! Пример: Отрезки на одной прямой и пересекаются в одной точке")
p1 = Point(0, 2)
p2 = Point(2, 8)
p3 = Point(2, 8)
p4 = Point(3, 11)
s1 = Section(p1, p2)
s2 = Section(p3, p4)
print(s1 == s2, "Равенство длин отрезков")
print(s1 < s2, "Сравнение длин отрезков - первый короче второго")
print(s1 > s2, "Сравнение длин отрезков - первый длиннее второго")
print(s1.cross(s2))

print("! Пример: Отрезки на одной прямой и имеют множество точек пересечения")
p1 = Point(0, -1)
p2 = Point(3, 5)
p3 = Point(1, 1)
p4 = Point(-1, -3)
s1 = Section(p1, p2)
s2 = Section(p3, p4)
print(s1 == s2, "Равенство длин отрезков")
print(s1 < s2, "Сравнение длин отрезков - первый короче второго")
print(s1 > s2, "Сравнение длин отрезков - первый длиннее второго")
print(s1.cross(s2))

print("! Пример: Отрезки лежат на одной прямой не пересекаются")
p1 = Point(-1, -3)
p2 = Point(0, -1)
p3 = Point(2, 3)
p4 = Point(4, 7)
s1 = Section(p1, p2)
s2 = Section(p3, p4)
print(s1 == s2, "Равенство длин отрезков")
print(s1 < s2, "Сравнение длин отрезков - первый короче второго")
print(s1 > s2, "Сравнение длин отрезков - первый длиннее второго")
print(s1.cross(s2))

print("! Пример: отрезки пересекаются")
p1 = Point(0, -1)
p2 = Point(3, 5)
p3 = Point(-1, 4)
p4 = Point(5, 1)
s1 = Section(p1, p2)
s2 = Section(p3, p4)
print(s1 == s2, "Равенство длин отрезков")
print(s1 < s2, "Сравнение длин отрезков - первый короче второго")
print(s1 > s2, "Сравнение длин отрезков - первый длиннее второго")
print(s1.cross(s2))

print("! Пример: Прямая паралельна оси ординат x = 2")
p1 = Point(2, -1)
p2 = Point(2, 2)
p3 = Point(2, 1)
p4 = Point(2, 3)
s1 = Section(p1, p2)
s2 = Section(p3, p4)
print(s1 == s2, "Равенство длин отрезков")
print(s1 < s2, "Сравнение длин отрезков - первый короче второго")
print(s1 > s2, "Сравнение длин отрезков - первый длиннее второго")
print(s1.cross(s2))

print("! Пример: Прямая паралельна оси абсцисс y = 2")
p1 = Point(2, 2)
p2 = Point(0, 2)
p3 = Point(3, 2)
p4 = Point(4, 2)
s1 = Section(p1, p2)
s2 = Section(p3, p4)
print(s1 == s2, "Равенство длин отрезков")
print(s1 < s2, "Сравнение длин отрезков - первый короче второго")
print(s1 > s2, "Сравнение длин отрезков - первый длиннее второго")
print(s1.cross(s2))


class Triangle:

    def __init__(self, *args):
        coord_list = []
        for i in range(len(args)):
            if isinstance(args[i], Point):
                coord_list.append((args[i].x, args[i].y))
            elif isinstance(args[i], Section):
                coord_list.append((args[i].x1, args[i].y1))
                coord_list.append((args[i].x2, args[i].y2))
            else:
                raise TypeError("Класс Triangle принимает только точки и отрезки")
        self.r = list(set(coord_list))
        if len(self.r) != 3:
            print("Из этого треугольник не построить")
            self.is_triangle()
        self.x1 = self.r[0][0]
        self.x2 = self.r[1][0]
        self.x3 = self.r[2][0]
        self.y1 = self.r[0][1]
        self.y2 = self.r[1][1]
        self.y3 = self.r[2][1]
        self.a = self._side_lenght(self.r[0], self.r[1])
        self.b = self._side_lenght(self.r[1], self.r[2])
        self.c = self._side_lenght(self.r[2], self.r[0])

    @staticmethod
    def _side_lenght(a, b):
        return round(((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5, 2)

    def is_triangle(self):
        if (self.r[0][0] == self.r[1][0] and self.r[1][0] != self.r[2][0]) or (
                self.r[0][1] == self.r[1][1] and self.r[1][1] != self.r[2][1]):
            return True
        if len(self.r) != 3 or (
                (self.r[2][0] - self.r[0][0]) / (self.r[1][0] - self.r[0][0]) == (self.r[2][1] - self.r[0][1]) / (
                self.r[1][1] - self.r[0][1])):
            print("Жаль! но треугольник не получится")
            return False
        return True

    def perimeter(self):
        if not self.is_triangle():
            return False
        per = round((self.a + self.b + self.c), 2)
        return per

    def square(self):
        if not self.is_triangle():
            return False
        k = (self.a + self.b + self.c) / 2
        sq = (k * (k - self.a) * (k - self.b) * (k - self.c)) ** 0.5
        return round(sq, 2)

    def mediana(self):
        if not self.is_triangle():
            return False
        me = round((((2 * self.b ** 2 + 2 * self.c ** 2 - self.a ** 2) / 4) ** 0.5), 2)
        return me

    def angle_type(self):
        if not self.is_triangle():
            return False
        sides = [self.a, self.b, self.c]
        sides.sort()
        print(sides)
        if round(sides[2] ** 2) == round((sides[0] ** 2 + sides[1] ** 2)):
            print("Треугольник прямоугольный")
        elif sides[2] ** 2 < sides[0] ** 2 + sides[1] ** 2:
            print("Треугольник остроугольный")
        else:
            print("Треугольник тупоугольный")

    def draw(self):
        # print(matplotlib.get_backend())
        fig = plt.figure()
        ax = fig.add_subplot(111)
        fig.set(facecolor="violet")
        ax.set(facecolor="pink")
        ax.set_xlim([-5, 10])
        ax.set_ylim([-5, 10])
        ax.set_title("Построение треугольника")
        ax.title.set_color("blue")
        ax.title.set_size(18)
        ax.set_xlabel("Ось абcцисс")
        ax.set_ylabel("Ось ординат")
        ax.plot([self.x1, self.x2, self.x3, self.x1], [self.y1, self.y2, self.y3, self.y1])
        ax.scatter([self.x1, self.x2, self.x3], [self.y1, self.y2, self.y3])
        # ax.plot([self.r[x][0] for x in range(len(self.r))], [self.r[x][1] for x in range(len(self.r))])
        # ax.scatter([self.r[x][0] for x in range(len(self.r))], [self.r[x][1] for x in range(len(self.r))])
        plt.show()


print("!Пример: Треугольник прямоугольный")
k1 = Point(0, 1)
k2 = Point(0, 6)
k3 = Point(6, 1)
t = Triangle(k1, k2, k3)
print(t.perimeter(), "ед. - Периметр треугольника", )
print(t.mediana(), "ед. - Медина к стороне а в тругольнике")
print(t.square(), "кв.ед. - Площадь треугольника")
print(t.angle_type())
t.draw()

print("!Пример: Треугольник тупоугольный")
k1 = Point(0, 1)
k2 = Point(-2, 6)
k3 = Point(6, 1)
t = Triangle(k1, k2, k3)
print(t.perimeter(), "ед. - Периметр треугольника", )
print(t.mediana(), "ед. - Медина к стороне а в тругольнике")
print(t.square(), "кв.ед. - Площадь треугольника")
print(t.angle_type())
t.draw()

print("!Пример: Треугольник задан тремя отрезками и остроугольный")
k1 = Point(-2, -2)
k2 = Point(2, 6)
k3 = Point(6, 1)
a = Section(k1, k2)
b = Section(k2, k3)
c = Section(k3, k1)
t = Triangle(a, b, c)
print(t.perimeter(), "ед. - Периметр треугольника", )
print(t.mediana(), "ед. - Медина к стороне а в тругольнике")
print(t.square(), "кв.ед. - Площадь треугольника")
print(t.angle_type())
t.draw()
print("!Пример: Треугольник задан отрезком и точкой")
k1 = Point(0, 1)
k2 = Point(-2, 6)
k3 = Point(6, 1)
a = Section(k1, k2)
t = Triangle(k3, a)
print(t.perimeter(), "ед. - Периметр треугольника", )
print(t.mediana(), "ед. - Медина к стороне а в тругольнике")
print(t.square(), "кв.ед. - Площадь треугольника")
print(t.angle_type())
t.draw()

print("!Пример: Треугольник задан двумя отрезками")
k1 = Point(-3, 8)
k2 = Point(0, 2)
k3 = Point(7, 5)
a = Section(k1, k2)
b = Section(k2, k3)
t = Triangle(a, b)
print(t.perimeter(), "ед. - Периметр треугольника", )
print(t.mediana(), "ед. - Медина к стороне а в тругольнике")
print(t.square(), "кв.ед. - Площадь треугольника")
print(t.angle_type())
t.draw()

print("!Пример: Треугольник нельзя построить, три точки на одной прямой")
k1 = Point(0, 1)
k2 = Point(-2, -3)
k3 = Point(3, 7)
t = Triangle(k1, k2, k3)
print(t.perimeter(), "ед. - Периметр треугольника", )
print(t.mediana(), "ед. - Медина к стороне а в тругольнике")
print(t.square(), "кв.ед. - Площадь треугольника")
print(t.angle_type())
t.draw()

print("!Пример:  Треугольник нельзя построить, три отрезка не замыкаются")
k1 = Point(-3, 8)
k2 = Point(0, 2)
k3 = Point(5, 5)
k4 = Point(9, 2)
a = Section(k1, k2)
b = Section(k2, k3)
c = Section(k3, k4)
t = Triangle(a, b, c)
print(t.perimeter(), "ед. - Периметр треугольника", )
print(t.mediana(), "ед. - Медина к стороне а в тругольнике")
print(t.square(), "кв.ед. - Площадь треугольника")
print(t.angle_type())
t.draw()


class Quad(Section, Triangle):

    def __init__(self, *args):
        coord_list = []
        for c in range(len(args)):
            if isinstance(args[c], Point):
                coord_list.append((args[c].x, args[c].y))
            elif isinstance(args[c], Section):
                coord_list.append((args[c].x1, args[c].y1))
                coord_list.append((args[c].x2, args[c].y2))
            else:
                raise TypeError("Класс Quad принимает только точки и отрезки")
        print(coord_list)
        self.r = []
        set_h = list(set(coord_list))
        for x in coord_list:
            if x in set_h:
                self.r.append(x)
                set_h.remove(x)
        print(self.r)
        if len(self.r) != 4:
            raise ValueError("Из этого построить четырехугольник нельзя")
        self.a = self._side_lenght(self.r[0], self.r[1])
        self.b = self._side_lenght(self.r[1], self.r[2])
        self.c = self._side_lenght(self.r[2], self.r[3])
        self.d = self._side_lenght(self.r[3], self.r[0])

    @staticmethod
    def _side_lenght(a, b):
        return round((((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5), 2)

    @staticmethod
    def _s_l(a, b, c):
        if (b[0] == a[0] and b[0] != c[0]) or (b[1] == a[1] and b[1] != c[1]):
            return False
        elif (c[0] - a[0]) / (b[0] - a[0]) == (c[1] - a[1]) / (b[1] - a[1]):
            print("!!! Четырехугольник нельзя построить!!!")
            return True

    def is_quad(self):
        if len(self.r) != 4 or self._s_l(self.r[0], self.r[1], self.r[2]) or self._s_l(
                self.r[0], self.r[1], self.r[3]) or self._s_l(self.r[1], self.r[2], self.r[3]):
            return False
        return True

    def perimeter(self):
        if not self.is_quad():
            return False
        per = self.a + self.b + self.c + self.d
        return per

    def quad_type(self):
        self.d1 = Section(Point(*self.r[0]), Point(*self.r[2]))
        self.d2 = Section(Point(*self.r[1]), Point(*self.r[3]))
        if self.d1.cross(self.d2) == True:
            self.type = "Четырехугольник выпуклый"
        else:
            self.type = "Четырехугольник не выпуклый"
        return self.type

    def quad_square(self):
        if self.type == "Четырехугольник выпуклый":
            a = Section(Point(*self.r[0]), Point(*self.r[1]))
            b = Section(Point(*self.r[1]), Point(*self.r[2]))
            c = Section(Point(*self.r[2]), Point(*self.r[3]))
            d = Section(Point(*self.r[3]), Point(*self.r[0]))
            tr1 = Triangle(a, b, self.d1)
            tr2 = Triangle(c, d, self.d1)
            sq = round(tr1.square() + tr2.square(), 2)
            return f"{sq} кв.ед. - Площадь этого выпуклого четырехугольника"

    def draw(self):

        fig = plt.figure()
        ax = fig.add_subplot(111)
        fig.set(facecolor="violet")
        ax.set(facecolor="pink")
        ax.set_xlim([-5, 10])
        ax.set_ylim([-5, 10])
        ax.set_title("Построение четырехугольника")
        ax.title.set_color("blue")
        ax.title.set_size(18)
        ax.set_xlabel("Ось абcцисс")
        ax.set_ylabel("Ось ординат")
        ax.plot([self.r[0][0], self.r[1][0], self.r[2][0], self.r[3][0], self.r[0][0]],
                [self.r[0][1], self.r[1][1], self.r[2][1], self.r[3][1], self.r[0][1]])
        ax.scatter([self.r[0][0], self.r[1][0], self.r[2][0], self.r[3][0], self.r[0][0]],
                   [self.r[0][1], self.r[1][1], self.r[2][1], self.r[3][1], self.r[0][1]])
        plt.show()


print("! Пример: Четырехугольник задан 4 точками")
k1 = Point(-2, 0)
k2 = Point(-2, 6)
k3 = Point(6, 3)
k4 = Point(6, 0)
w = Quad(k1, k2, k3, k4)
print(w.quad_type())
print(w.perimeter(), "- Периметр четырехугольника'")
print(w.quad_square())
w.draw()

print("! Пример: Четырехугольник задан четырьмя отрезками")
k1 = Point(-2, 0)
k2 = Point(0, 6)
k3 = Point(7, 8)
k4 = Point(6, 0)
s1 = Section(k1, k2)
s2 = Section(k2, k3)
s3 = Section(k3, k4)
s4 = Section(k4, k1)
w = Quad(s1, s2, s3, s4)
print(w.quad_type())
print(w.perimeter(), "- Периметр четырехугольника'")
print(w.quad_square())
w.draw()

print("! Пример: Четырехугольник задан точкой и двумя отрезками")
k1 = Point(-2, -2)
k2 = Point(-1, 4)
k3 = Point(4, 8)
k4 = Point(6, 2)
s1 = Section(k2, k3)
s2 = Section(k3, k4)
w = Quad(k1, s1, s2)
print(w.quad_type())
print(w.perimeter(), "- Периметр четырехугольника'")
print(w.quad_square())
w.draw()

print("! Пример: Четырехугольник нельзя построить, три точки на одной прямой")
k1 = Point(0, 1)
k2 = Point(-2, -3)
k3 = Point(3, 7)
k4 = Point(5, 5)
w = Quad(k1, k2, k3, k4)
print(w.quad_type())
print(w.perimeter(), "- Периметр четырехугольника'")
print(w.quad_square())
w.draw()

print("! Пример: Четырехугольник задан 4 отрезками, не замыкаются")
k1 = Point(-2, -2)
k2 = Point(-1, 4)
k3 = Point(4, 8)
k4 = Point(6, 2)
k5 = Point(3, -1)
s1 = Section(k1, k2)
s2 = Section(k2, k3)
s3 = Section(k3, k4)
s4 = Section(k4, k5)
w = Quad(s1, s2, s3, s4)
print(w.quad_type())
print(w.perimeter(), "- Периметр четырехугольника'")
print(w.quad_square())
w.draw()
