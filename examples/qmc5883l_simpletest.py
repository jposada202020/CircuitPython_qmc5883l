# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT
import time
import board
import circuitpython_qmc5883l as qmc5883

i2c = board.I2C()
qmc = qmc5883.QMC5883L(i2c)

qmc.oversample = qmc5883.OVERSAMPLE_128
qmc.field_range = qmc5883.FIELDRANGE_2G
qmc.output_data_rate = qmc5883.OUTPUT_DATA_RATE_200
qmc.mode_control = qmc5883.MODE_CONTINUOUS

for i in range(50):
    mag_x, mag_y, mag_z = qmc.magnetic
    print("x:{}Gs, y:{}Gs, z{}Gs".format(mag_x, mag_y, mag_z))
    time.sleep(0.3)
