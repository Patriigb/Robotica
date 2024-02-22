#!/usr/bin/python
# -*- coding: UTF-8 -*-
import argparse
import numpy as np
import time
from Robot import Robot
import matplotlib.pyplot as plt
import os

def plot(robot):
    # Leer el archivo y extraer los datos
    timestamps = []
    x_coords = []
    y_coords = []

    with open(robot.log_file, 'r') as file:
        for line in file:
            parts = line.split()
            timestamps.append(float(parts[0]))
            x_coords.append(float(parts[1]))
            y_coords.append(float(parts[2]))

    # Trazar el recorrido
    plt.figure(figsize=(8, 6))
    plt.plot(x_coords, y_coords, marker='o', linestyle='-')
    plt.title('Recorrido del Robot')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.grid(True)

    # Guardar el gráfico en un archivo
    ruta, _ = os.path.splitext(robot.log_file)  # Separa la ruta y la extensión del archivo
    plot_file = ruta + ".png"  # Cambia la extensión a .png
    plt.savefig(plot_file)  # Cambia el nombre del archivo según lo desees

def main(args):
    try:
        if args.radioD < 0:
            print('d must be a positive value')
            exit(1)

        p = input()
        # Instantiate Odometry. Default value will be 0,0,0
        # robot = Robot(init_position=args.pos_ini)
        robot = Robot()

        print("X value at the beginning from main X= %.2f" %(robot.x.value))
        # 1. launch updateOdometry Process()
        robot.startOdometry()

        # 2. perform trajectory


        # Linea recta
        robot.setSpeed(10,0)
        print("Start : %s" % time.ctime())
        time.sleep(4)
        print("X value from main tmp %d" % robot.x.value)
        robot.lock_odometry.acquire()
        print("Odom values at main at the END: %.2f, %.2f, %.2f " % (robot.x.value, robot.y.value, robot.th.value))
        robot.lock_odometry.release()

        robot.stopOdometry()

        p = input()
        # Solo w (circulo)
        robot.startOdometry()
        robot.setSpeed(0, 4)
        print("Start : %s" % time.ctime())
        time.sleep(4)
        print("X value from main tmp %d" % robot.x.value)
        robot.lock_odometry.acquire()
        print("Odom values at main at the END: %.2f, %.2f, %.2f " % (robot.x.value, robot.y.value, robot.th.value))
        robot.lock_odometry.release()
        time.sleep(4)
        print("End : %s" % time.ctime())

        robot.lock_odometry.acquire()
        print("Odom values at main at the END: %.2f, %.2f, %.2f " % (robot.x.value, robot.y.value, robot.th.value))
        robot.lock_odometry.release()

        robot.stopOdometry()

        p = input()
        # 90º
        robot.startOdometry()
        robot.setSpeed(0, 0.78)
        print("Start : %s" % time.ctime())
        time.sleep(2)
        print("X value from main tmp %d" % robot.x.value)
        robot.lock_odometry.acquire()
        print("Odom values at main at the END: %.2f, %.2f, %.2f " % (robot.x.value, robot.y.value, robot.th.value))
        robot.lock_odometry.release()
        time.sleep(2)
        print("End : %s" % time.ctime())

        robot.lock_odometry.acquire()
        print("Odom values at main at the END: %.2f, %.2f, %.2f " % (robot.x.value, robot.y.value, robot.th.value))
        robot.lock_odometry.release()

        robot.stopOdometry()

        # ...



        # 3. wrap up and close stuff ...
        # This currently unconfigure the sensors, disable the motors,
        # and restore the LED to the control of the BrickPi3 firmware.
        robot.stopOdometry()


    except KeyboardInterrupt:
    # except the program gets interrupted by Ctrl+C on the keyboard.
    # THIS IS IMPORTANT if we want that motors STOP when we Ctrl+C ...
        robot.stopOdometry()

if __name__ == "__main__":

    # get and parse arguments passed to main
    # Add as many args as you need ...
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--radioD", help="Radio to perform the 8-trajectory (mm)",
                        type=float, default=40.0)
    args = parser.parse_args()

    main(args)



