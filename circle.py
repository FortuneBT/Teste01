from math import pi

def circle(rayon):
    return pi*(rayon**2)

cercles = [3, 7, pi, 0,5 ,12, 46, 1]
circonference = 0
rayon = 0

for rayon in cercles:
    circonference = circle(rayon)
    print(f"Pour un rayon de {rayon}, la circonférence de ce cercle est de {circonference}")

