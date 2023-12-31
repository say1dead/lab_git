def area(a, h):
    '''
    Возвращает площадь треугольника.

        Параметры:
            a (float) - сторона треугольника
            h (float) - высота треугольника на сторону a

        Возвращаемое значение:
            Произведение стороны a на высоту h деленное на 2
    '''
    return a * h / 2

def perimetr(a, b, c):
    '''
    Возвращает периметр треугольника.

        Параметры:
            a (float) - первая сторона треугольника
            b (float) - вторая сторона треугольника
            c (float) - третья сторона треугольника

        Возвращаемое значение:
            Сумму трех сторон
    '''
    return a + b + c