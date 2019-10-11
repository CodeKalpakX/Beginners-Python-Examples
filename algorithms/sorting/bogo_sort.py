# Simple Bogo-Sort-Algorithm

import random

def bogosort(liste):
        while not isSorted(liste):
                random.shuffle(liste)
        return liste

def isSorted(liste):
        for i in range(len(liste)):
                if not i==len(liste)-1:
                        if liste[i]>liste[i+1]:
                                return False
                elif liste[i]<liste[i-1]:
                        return False
        return True
