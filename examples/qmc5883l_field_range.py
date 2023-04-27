# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT
import time
import board
import qmc5883l

i2c = board.I2C()
qmc = qmc5883l.QMC5883L(i2c)

while True:
    for field_range in qmc5883l.field_range_values:
        print("Current Field Range Setting: ", qmc.field_range)
        for _ in range(10):
            mag_x, mag_y, mag_z = qmc.magnetic
            print("x:{:.2f}Gs, y:{:.2f}Gs, z{:.2f}Gs".format(mag_x, mag_y, mag_z))
            time.sleep(0.5)
        qmc.field_range = field_range
