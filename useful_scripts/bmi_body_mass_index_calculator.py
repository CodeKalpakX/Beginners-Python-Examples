#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys

# BMI calculator
# f(w, h) = w / h ** 2 
# w refers to weight, h refers to height
# weight is in kilograms(kg's), height in meters(m) standard metrics

body_mass_index = lambda w, h: round((w) / ((h  * 0.01) ** 2), 1)

# Test
# Playing/Testing Interface
i = 0
while True:
	if raw_input("\n[{}] Exit(press e) or To count BMI(press c):".format(i)).strip().lower() == "c":
		cal = body_mass_index(float(raw_input('\nWeight(in kgs)?: ')), float(raw_input('Height (in cm)?: ')))
		
		print("\nHealthy BMI ranges between 19 to 25:")
		print("Status: ")
		if cal >= 19 and cal <= 25:
			print("Your BMI: " + str(cal) + "\n  You are HEALTHY")
		elif cal < 19: 
			print("Your BMI: " + str(cal) + "\n  Your BodyMassIndex is Underweight\n  Not between Healthy range")
		else:
			print("Your BMI: " + str(cal) + "\n  Your BodyMassIndex is Overweight\n  Not between Healthy range")
		i += 1	
	
	else :
		sys.exit()
