# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

""" Based in example found in
https://github.com/adafruit/Adafruit_CircuitPython_LSM303DLH_Mag/blob/main/examples/lsm303dlh_mag_compass.py
"""
import time
from math import atan2, degrees
import board
import qmc5883l as qmc5883

i2c = board.I2C()
qmc = qmc5883.QMC5883L(i2c)


def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle = angle + 360
    return angle


def get_heading(sensor):
    mag_x, mag_y, _ = sensor.magnetic
    return vector_2_degrees(mag_x, mag_y)


while True:
    print("heading: {:.2f} degrees".format(get_heading(qmc)))
    time.sleep(0.2)
