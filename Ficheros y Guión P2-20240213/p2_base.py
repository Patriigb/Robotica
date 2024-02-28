#!/usr/bin/python
# -*- coding: UTF-8 -*-
import argparse
import numpy as np
import time
import math
import robotics as rb
import movimientos as mv
from Robot import Robot




def main(args):
    try:
        print(args.radioD)
        if args.radioD < 0:
            print('d must be a positive value')
            exit(1)

        # Instantiate Odometry. Default value will be 0,0,0
        # robot = Robot(init_position=args.pos_ini)
        robot = Robot()
        print("X value at the beginning from main X= %.2f" %(robot.x.value))
        # 1. launch updateOdometry Process()
        
        
        if args.tray == 1:
            mv.movimento_8(robot, 2.5, args.radioD)

        elif args.tray == 2:
            mv.movimiento_cadena(robot, args.radioD, args.radioA, 2.5)
            
        else:
            print("Trayectoria seleccionada incorrecta")


    except KeyboardInterrupt:
    # except the program gets interrupted by Ctrl+C on the keyboard.
    # THIS IS IMPORTANT if we want that motors STOP when we Ctrl+C ...
        robot.stopOdometry()

if __name__ == "__main__":

    # get and parse arguments passed to main
    # Add as many args as you need ...
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--radioD", help="Radio to perform the 8-trajectory or chain trajectory (mm)",
                        type=float, default=40.0)   # radio de la curva
    parser.add_argument("-a", "--radioA", help="Radio to perform the chain-trajectory (mm)",
                        type=float, default=20.0)
    parser.add_argument("-m", "--tray", help="Trajectory (1 -> 8-trajectory // 2 -> chain-trajectory)",
                        type=int)
    args = parser.parse_args()

    main(args)





