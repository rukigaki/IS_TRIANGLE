class MyException(Exception):
    """
    Исключение, которое отлавливает числа
    в диапозоне от минус бесконечности до 1 невключительно
    """
    pass


def recursion_function(side):
    try:
        value_local = int(input("Введите натуральное целочисленное число " + side + ": "))
        if value_local < 1:
            raise MyException
    except ValueError:
        value_local = recursion_function(side)
    except MyException:
        value_local = recursion_function(side)
    return value_local


def is_triangle(values_sides):
    max_side = values_sides.pop(values_sides.index(max(values_sides)))  # Поиск наибольшей стороны
    if max_side > sum(values_sides):
        print("Увы, но треугольник с такими сторонами не построишь")
    else:
        print("Да, вы можете построить треугольник")


sides = []
for name_side in ["a", "b", "c"]:
    try:
        value = int(input("Введите сторону " + name_side + ": "))
        if value < 1:
            raise MyException
    except ValueError:
        value = recursion_function(name_side)
    except MyException:
        value = recursion_function(name_side)
    sides.append(value)


is_triangle(sides)
