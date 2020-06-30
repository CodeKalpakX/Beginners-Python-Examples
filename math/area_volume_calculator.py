#!/usr/bin/python
# -*- coding: utf-8 -*-


import math
import sys

# Perimeter
# or sum of span of all sides of figure

# perimeter of square f(s) = 4 * s
# where s is the side of square
peri_of_square = lambda s: 4 * s

# perimeter of rectangle, f(L, W) = 2 * (L + W) or 2L + 2W
# where L is length, and W is width(breadth) of rectangle
peri_of_rectangle = lambda l, w: 2 * (l + w)

# perimeter of triangle, f(s1, s2, s3) = s1 + s2 + s3
# where s1, s2, s3, are the sides of a regular triangle
peri_of_triangle = lambda s1, s2, s3: s1 + s2 + s3

# peri of right angled triangle, f(a, b) = a + b + square_root(a ** 2 + b ** 2)
# since, by pythagoras theoram,
#  a ** 2 + b ** 2 = c ** 2 or a squared + b squared = c squared
peri_of_rt_triangle = lambda a, b: a + b + math.sqrt(a ** 2 + b ** 2)

# perimeter of circle(or circumference), f(r) = 2 * r * pi
# or f(d) = d * pi, where r is radius, pi is pi ratio(3.14159......), 
# d is diameter
peri_of_circle = lambda r: 2 * r * math.pi
peri_of_circle1 = lambda d: d * math.pi 


# Areas
# or surface area of figure
# how many lengths into widths and vice versa

# area of square, f(s) = s * s or (s)squared or s ** 2
# where s is the side of square, s is same as both
# length and width of square
area_of_square = lambda s: s ** 2

# area of rectangle, f(L, W) = L * W
# or length multiplied by width(breadth)
area_of_rectangle = lambda l, w: l * w


# area of triangle, f(b, h) = b * h / 2
# where, b is base, and h is the height of triangle
# see: explaination of area of triangle
# here: 
area_of_triangle = lambda b, h: (b * h) / 2

# Heron's formula
# see for more info: https://en.wikipedia.org/wiki/Heron%27s_formula
area_of_triangle1 = lambda a, b, c: math.sqrt((a+b+c)/2 * ((a+b+c)/2 - a) ((a+b+c)/2 - b) ((a+b+c)/2 - c))

# area of parallelogram, f(b, h) = b * h
# where b is base, h is height of parallelogram	
area_of_parallelogram = lambda b, h: b * h 

# area of trapezoid(trapezium), f(b1, b2, h) (b1 + b2) / 2 * h
# where, b1 is base 1, b2 is base 2, and h is height
area_of_trapezoid = lambda b1, b2, h: (b1 + b2) / 2 * h

# area of circle, f(r) = pi * r ** 2
# where r is radius, pi is math constant of pi(C/D)
# see explaination of formula: 
# http://pythagoreanmath.com/complete-explanation-for-area-of-a-circle-formula/
area_of_circle = lambda r: math.pi * r ** 2


# Terminal UI
i = 0
while True:
	if raw_input("\n[{}] Exit(press e), Continue(press c): ".format(i)).lower() == "c":
		
		which_fig = raw_input("\nSquare(s), Rectangle(r), Triangle(t), right(|_)led triangle(rt), Parallelogram(pa), Cricle(ci), Trapezoid(tr): ").lower()

		if which_fig == "s":
			if raw_input("\nArea(press a) or Perimeter(press p): ").lower() == "a":
				print("\tArea of square: " + str(area_of_square(float(raw_input("Side of square: ")))))
			else:
				print("\tPerimeter of square: " + str(peri_of_square(float(raw_input("Side: ")))))

		elif which_fig == "r":
			if raw_input("\nArea(press a) or Perimeter(press p): ").lower() == "a":
				print("\tArea of rectangle: " + str(area_of_rectangle(float(raw_input("Length: ")), float(raw_input("Width: ")))))
			else:
				print("\tPerimeter of rectangle: " + str(peri_of_rectangle(float(raw_input("Length: ")), float(raw_input("Width: ")))))

		elif which_fig == "t":
			if raw_input("\nArea(press a) or Perimeter(press p): ").lower() == "a":
				if raw_input("\nBy Heron's Formula[y/n]: ").lower() == "y":
					print("\tArea of triangle(Heron's Formula): " + str(area_of_triangle1(float(raw_input("A: ")), float(raw_input("B: ")), float(raw_input("C: ")))))
				else:
					print("\tArea of triangle: " + str(area_of_triangle(float(raw_input("Base: ")), float(raw_input("Height: ")))))
			else:
				print("\tPerimeter of triangle: " + str(peri_of_triangle(float(raw_input("A: ")), float(raw_input("B: ")), float(raw_input("C: ")))))
		
		elif which_fig == "rt":
			if raw_input("\nArea(press a) or Perimeter(press p): ").lower() == "a":
				print("\tArea of triangle: " + str(area_of_triangle(float(raw_input("Base: ")), float(raw_input("Height: ")))))
			else:
				print("\tPerimeter or right angled triangle: " + str(peri_of_rt_triangle(float(raw_input("A: ")), float(raw_input("B: ")))))
			
		elif which_fig == "pa":
			if raw_input("\nArea(press a) or Perimeter(press p): ").lower() == "a":
				print("\tArea of parallelogram: " + str(area_of_parallelogram(float(raw_input("Base: ")), float(raw_input("Height: ")))))
			else:
				print("\tPerimeter of parallelogram: " + str(peri_of_rectangle(float(raw_input("Length: ")), float(raw_input("Width: ")))))
		
		elif which_fig == "tr":
			if raw_input("\nArea(press a) or Perimeter(press p): ").lower() == "a":
				print("\tArea of trapezoid: " + str(area_of_trapezoid(float(raw_input("Base 1: ")), float(raw_input("Base 2: ")), float(raw_input("Height: ")))))
			else:
				print("\tPerimeter of trapezoid: " + str(peri_of_triangle(float(raw_input("Side1: ")), float(raw_input("Side4: ")), float(raw_input("Side3: "))) + float(raw_input("Side1: "))))
			
		elif which_fig == "c":
			if raw_input("\nArea(press a) or Perimeter(press p): ").lower() == "a":
				print("\tArea of circle: " + str(area_of_circle(float(raw_input("Radius: ")))))
			else:
				if raw_input("\nUsing Radius(r) or Diameter(d): ").lower() == "r":
					print("\tCircumference of circle: " + str(peri_of_circle(float(raw_input("Radius: ")))))
				else:
					print("\tCircumference of circle: " + str(peri_of_circle1(float(raw_input("Diameter: ")))))

		i += 1

	else:
		sys.exit()
