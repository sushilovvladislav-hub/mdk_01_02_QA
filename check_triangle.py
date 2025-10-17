from math import isclose

def check_triagnle_type():
    

    print("Программа для определения типа")
    print("=" * 40)

    side1 = float(input("Введите сторону 1: ").strip())
    side2 = float(input("Введите сторону 2: ").strip())
    side3 = float(input("Введите сторону 3: ").strip())

    sides = sorted([side1, side2, side3])
    a, b, c = sides

    if a <= 0 or b <= 0 or c <= 0:
        return "Все стороны должны быть больше нуля"

    if a + b <= c or isclose(a + b, c, rel_tol=1e-9):
        return "Треугольник с такими сторонами не существует"
        
    if isclose(a ** 2 + b ** 2, c ** 2, rel_tol=1e-9):
        return "Прямоугольный треугольник"

    elif (isclose(a, b, rel_tol=1e-9) and
          isclose(b, c, rel_tol=1e-9)):
        return "Равносторонний треугольник"

    elif (isclose(a, b, rel_tol=1e-9) or
        isclose(b, c, rel_tol=1e-9) or
        isclose(a, c, rel_tol=1e-9)):
        return "Равнобедренный треугольник"
    
    else:
        return "Разносторонний треугольник"



if __name__ == "__main__":
    result = check_triagnle_type()
    print(f"\nРезультат: {result}")