# Fichero python que contiene las funciones correspondientes a los movimientos del robot

# Importamos las librerias necesarias
import argparse
import numpy as np
import time
import math
import robotics as rb
from Robot import Robot

def movimento_8(p, robot):
    p = input()
    robot.startOdometry()
    # girar 90º
    nextStep = False
    x,  y, theta_ini = robot.readOdometry()
    robot.setSpeed(0, -1)
    while not nextStep:
            x,  y, theta = robot.readOdometry()
            # print("th", rb.norm_pi(theta - theta_ini), "min", -math.pi/2 - 0.05, "max", -math.pi/2 + 0.05)
            if theta != 0:
                if rb.norm_pi(theta - theta_ini) > -math.pi/2 - 0.05  and \
                    rb.norm_pi(theta - theta_ini) < -math.pi/2 + 0.05:
                    nextStep = True


# Función para calcular los puntos de tangencia entre dos circunferencias en el ejes de coordenadas
def movimiento_2_tangentes_puntos(r1, r2, d):
    n = 0
    # Coordenadas del ciruclo de la izquierda en el eje de coordenadas
    x1 = 10
    y1 = 0

    # Coordenadas del ciruclo de la derecha en el eje de coordenadas
    x2 = x1 + d
    y2 = 0

    # Cálculo de las coordenadas X de los puntos tangentes
    x_tangente = (x1 + x2) / 2

    # Cálculo de las coordenadas Y de los puntos tangentes
    y_tangente_sup = math.sqrt(r2**2 - (d - x_tangente)**2) # √(r2² - (d - x_tangente)²)
    y_tangente_inf = -y_tangente_sup

    # Cálculo de las coordenadas de los puntos de tangencia
    x_tangente_sup = x_tangente
    x_tangente_inf = x_tangente
    y_tangente_sup = y_tangente_sup
    y_tangente_inf = y_tangente_inf

    return x_tangente_sup, y_tangente_sup, x_tangente_inf, y_tangente_inf
