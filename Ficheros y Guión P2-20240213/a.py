from math import pi, degrees

# Definir el ángulo total a girar en radianes
angulo_total = pi / 2

# Definir el tiempo total en segundos
tiempo_total = 2

w = angulo_total / tiempo_total
v=0
print(w)

r = 2.5
L = 10.7

speedDPS_left = degrees(v / r - (L * w) / (2 * r))
speedDPS_right = degrees(v / r + (L * w) / (2 * r))

print(speedDPS_left)
print(speedDPS_right)