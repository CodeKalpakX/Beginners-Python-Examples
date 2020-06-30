#!/usr/bin/python
# -*- coding: utf-8 -*-


# By formula derived by Euler(A great mathematician)
print("Euler's Formula: F(faces) + V(vertices) = E(Edges)+2\n")

# Further derivation
print("Derivation 1: E(Edges) = F(faces)+V(vertices) - 2")
print("Derivation 2: V(vertices) = E(edges)+2 - F(Faces)")
print("Derivation 3: F(faces) = E(edges)+2 - V(vertices)")


# By order of operations, parenthesis can be added 
# for ensuring, but not needed
def E(f, v):
	return f+v - 2

def V(e, f):
	return e+2 - f 

def F(e, v):
	return e+2 - v


# function to evaluate
# By default datatype of raw_input() is string
user = raw_input("\nE, V or F: ").upper()
print(" ")


# evaluating function asked by user
if user == "E":
	print("\nEdges: " + str(E(input("Faces: "), input("Vertices: "))))
elif user == "V":
	print("\nVertices: " + str(V(input("Edges: "), input("Faces: "))))
elif user == "F":
	print("\nFaces: " + str(F(input("Edges: "), input("Vertices: "))))
else:
	print("Invalid Input, Try again!")


# A while loop can be added 
# to perform multiple calculations
