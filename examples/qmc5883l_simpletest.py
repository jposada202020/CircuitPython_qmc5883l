# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT
import time
import board
import qmc5883l

i2c = board.I2C()
qmc = qmc5883l.QMC5883L(i2c)

while True:
    mag_x, mag_y, mag_z = qmc.magnetic
    print("x:{:.2f}Gs, y:{:.2f}Gs, z{:.2f}Gs".format(mag_x, mag_y, mag_z))
    time.sleep(0.3)
