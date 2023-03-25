# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT
# pylint: disable=protected-access
import time
import board
import circuitpython_qmc5883l as qmc5883


i2c = board.I2C()
qmc = qmc5883.QMC5883L(i2c)

print("Initial Configuration register", bin(qmc._conf_reg))
print("Setting Oversample to 64(0b11)")
qmc.oversample = qmc5883.OVERSAMPLE_64
print("Configuration register", bin(qmc._conf_reg))
print("Setting Oversample to 128(0b10)")
qmc.oversample = qmc5883.OVERSAMPLE_128
print("Configuration register", bin(qmc._conf_reg))
print("Setting Oversample to 2G (0b00)")
qmc.field_range = qmc5883.FIELDRANGE_2G
print("Configuration register", bin(qmc._conf_reg))
print("Setting Range to 8G (0b01)")
qmc.field_range = qmc5883.FIELDRANGE_8G
print("Configuration register", bin(qmc._conf_reg))
print("setting ouput Data Rate 100HZ (0b10)")
qmc.output_data_rate = qmc5883.OUTPUT_DATA_RATE_100
print("Configuration register", bin(qmc._conf_reg))
print("setting ouput Data Rate 200HZ (0b11)")
qmc.output_data_rate = qmc5883.OUTPUT_DATA_RATE_200
print("Configuration register", bin(qmc._conf_reg))
print("setting Mode to Continuous (0b01)")
qmc.mode_control = qmc5883.MODE_CONTINUOUS
print("Configuration register", bin(qmc._conf_reg))

for i in range(50):
    mag_x, mag_y, mag_z = qmc.magnetic
    print(mag_x, mag_y, mag_z)
    time.sleep(0.3)
