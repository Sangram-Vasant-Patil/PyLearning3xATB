# ✅ 2. Triangle Classifier:
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.
# 3 Input
# side 1, side 2 and side 3
# output - Eq, Iso, Scalene -
# Eq. = side 1 == side 2 = side 3

Side_1 = float(input("Enter the length of side 1: "))
Side_2 = float(input("Enter the length of side 2: "))
Side_3 = float(input("Enter the length of side 3: "))

if Side_1 == Side_2 == Side_3:
    print("Equilateral")
elif Side_1 == Side_2 or Side_3 == Side_2 or Side_1 == Side_3:
    print("Isosceles")
else:
    print("Scalene")

