# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import qmc5883l

i2c = board.I2C()
qmc = qmc5883l.QMC5883L(i2c)

while True:
    for data_rate in qmc5883l.data_rate_values:
        print("Current Data Rate Setting: ", qmc.output_data_rate)
        for _ in range(10):
            mag_x, mag_y, mag_z = qmc.magnetic
            print(f"x:{mag_x:.2f}Gs, y:{mag_y:.2f}Gs, z{mag_z:.2f}Gs")
            print()
            time.sleep(0.5)
        qmc.output_data_rate = data_rate
