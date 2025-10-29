import math
print("Enter dimensions of the trapezium:")
a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
h = float(input("Enter height (h): "))

r = float(input("\nEnter radius of the circle: "))

area_trapezium = 0.5 * (a + b) * h
area_circle = math.pi * (r ** 2)
area_shaded = area_trapezium - area_circle

print("\n--- AREA CALCULATIONS ---")
print(f"Area of Trapezium: {area_trapezium:.2f} square units")
print(f"Area of Circle: {area_circle:.2f} square units")
print(f"Area of Shaded Region: {area_shaded:.2f} square units")