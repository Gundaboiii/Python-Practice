def circle():
    radius = float(input("Enter Radius of the circle: "))
    area = 3.14 * radius * radius
    print("Area of the circle is: ", area)
def square():
    side = float(input("Enter side of the square: "))
    area = side * side
    print("Area of the square is: ", area)
def rectangle():
    length = float(input("Enter length of the rectangle: "))
    breadth = float(input("Enter breadth of the rectangle: "))
    area = length * breadth
    print("Area of the rectangle is: ", area)
def triangle():
    base = float(input("Enter base of the triangle: "))
    height = float(input("Enter height of the triangle: "))
    area = 0.5 * base * height
    print("Area of the triangle is: ", area)
print("Program to find the areas of different shapes")
option = int(input("1. Circle\t2.Square\t3.Rectangle\t4.Triangle\n"))
if option == 1:
    circle()
elif option == 2:
    square()
elif option == 3:
    rectangle()
elif option == 4:
    triangle()
else:
    print("Invalid option Entered!")
