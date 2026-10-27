from class_Octagon import Octagon

def main() -> None:
    try:
        side_input: str = input("Введите длину стороны октагона: ")
        side: float = float(side_input)
        
        if side <= 0:
            print("Ошибка: Сторона должна быть положительным числом.")
            return
   
        oct_obj = Octagon(side)
        
        print("Периметр октагона:", oct_obj.perimeter())
        print("Площадь октагона:", oct_obj.area())
        print("Радиус вписанной окружности:", oct_obj.inscribed_radius())
        print("Радиус описанной окружности:", oct_obj.circumscribed_radius())
        
        oct_obj.draw()
        
    except ValueError:
        print("Ошибка, пожалуйста, введите числовое значение.")

if __name__ == "__main__":
    main()