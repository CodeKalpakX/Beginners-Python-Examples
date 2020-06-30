#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

# Calculating thrust of Aircraft Propeller
def thrust_props(diameter , velocity , velocity1 , density):
    
    # According to formula
    return math.pi / 4 * diameter ** 2 * (velocity + velocity1/2) * density * velocity1

print('Hello Aircraft Lovers,\n')

while(True):
	# Loop for continous calculation
    start_or_end = str(raw_input('start or end : ')).strip().lower()
    
    # Main interface
    if start_or_end == 'start':
        res = thrust_props(float(input('\nDiameter of propeller: ')) , float(input('Velocity of air flow: ')) , float(input('Additional propeller acceleration, velocity: ')) , float(input('Fluid density: ')))
        print("\nThrust of propeller: {}".format(res)) 
    
    else:
        quit()
    print("")

# found formula on nasa's website
