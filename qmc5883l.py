# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya for Trinity
#
# SPDX-License-Identifier: MIT
"""
`qmc5883l`
================================================================================

CircuitPython driver for the qmc5883l magnetometer


* Author(s): Jose D. Montoya

Implementation Notes
--------------------


* Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
* Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register

"""

from micropython import const
from adafruit_bus_device import i2c_device
from adafruit_register.i2c_struct import ROUnaryStruct, UnaryStruct
from adafruit_register.i2c_bits import RWBits, ROBits

try:
    from busio import I2C
    from typing_extensions import NoReturn
except ImportError:
    pass

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/jposada202020/CircuitPython_qmc5883l.git"

_I2C_ADDR = const(0xD)
_REG_WHOAMI = const(0x0D)
_REG_SET_RESET = const(0x0B)
_REG_OPERATION_MODE = const(0x09)
_REG_STATUS = const(0x06)

OVERSAMPLE_64 = const(0b11)
OVERSAMPLE_128 = const(0b10)
OVERSAMPLE_256 = const(0b01)
OVERSAMPLE_512 = const(0b00)

FIELDRANGE_2G = const(0b00)
FIELDRANGE_8G = const(0b01)

OUTPUT_DATA_RATE_10 = const(0b00)
OUTPUT_DATA_RATE_50 = const(0b01)
OUTPUT_DATA_RATE_100 = const(0b10)
OUTPUT_DATA_RATE_200 = const(0b11)

MODE_STANDBY = const(0b00)
MODE_CONTINUOUS = const(0b01)

RESET_VALUE = const(0b01)


class QMC5883L:
    """Driver for the QMC5883L magnetometer connected over I2C.

    :param ~busio.I2C i2c_bus: The I2C bus the QMC5883L is connected to.
    :param int address: The I2C device address. Defaults to :const:`0xD`

    :raises RuntimeError: if the sensor is not found

    **Quickstart: Importing and using the device**

    Here is an example of using the :class:`QMC5883L` class.
    First you will need to import the libraries to use the sensor

        .. code-block:: python

            import board
            import circuitpython_qmc5883l.qmc5883l as qmc5883l

    Once this is done you can define your `board.I2C` object and define your sensor object

        .. code-block:: python

            i2c = board.I2C()  # uses board.SCL and board.SDA
            qmc = qmc5883l.QMC5883L(i2c)

    Now you have access to the :attr:`magnetic` attribute

        .. code-block:: python

            mag_x, mag_y, mag_z = qmc.magnetic


    """

    _device_id = ROUnaryStruct(_REG_WHOAMI, "H")
    _reset = UnaryStruct(_REG_SET_RESET, "H")
    _conf_reg = ROUnaryStruct(_REG_OPERATION_MODE, "H")
    _oversample = RWBits(2, _REG_OPERATION_MODE, 6)
    _field_range = RWBits(2, _REG_OPERATION_MODE, 4)
    _output_data_rate = RWBits(2, _REG_OPERATION_MODE, 2)
    _mode_control = RWBits(2, _REG_OPERATION_MODE, 0)
    _data_ready_register = ROBits(1, _REG_STATUS, 2)
    _x_LSB = ROUnaryStruct(0x00, "H")
    _x_MSB = ROUnaryStruct(0x01, "H")
    _y_LSB = ROUnaryStruct(0x02, "H")
    _y_MSB = ROUnaryStruct(0x03, "H")
    _z_LSB = ROUnaryStruct(0x04, "H")
    _z_MSB = ROUnaryStruct(0x05, "H")

    def __init__(self, i2c_bus: I2C, address: int = _I2C_ADDR) -> None:
        self.i2c_device = i2c_device.I2CDevice(i2c_bus, address)
        self.resolution = 12000

        if self._device_id != 0xFF:
            raise RuntimeError("Failed to find QMC5883L")
        self._reset = 0x01

    @property
    def oversample(self) -> int:
        """
        Over sample Rate (OSR) registers are used to control bandwidth of an
        internal digital filter. Larger OSR value leads to smaller filter bandwidth,
        less in-band noise and higher power consumption. It could be used to reach a
        good balance between noise and power.

        Four oversample ratios can be selected, 64, 128, 256 or 512. With the following
        global variables.

        +----------------------------------------+-------------------------+
        | Mode                                   | Value                   |
        +========================================+=========================+
        | :py:const:`qmc5883.OVERSAMPLE_64`      | :py:const:`0b11`        |
        +----------------------------------------+-------------------------+
        | :py:const:`qmc5883.OVERSAMPLE_128`     | :py:const:`0b10`        |
        +----------------------------------------+-------------------------+
        | :py:const:`qmc5883.OVERSAMPLE_256`     | :py:const:`0b01`        |
        +----------------------------------------+-------------------------+
        | :py:const:`qmc5883.OVERSAMPLE_512`     | :py:const:`0b00`        |
        +----------------------------------------+-------------------------+

        Example
        ---------------------

        .. code-block:: python

            i2c = board.I2C()
            qmc = qmc5883.QMC5883L(i2c)


            qmc.oversample = qmc5883.OVERSAMPLE_64

        """

        return self._oversample

    @oversample.setter
    def oversample(self, rate: int) -> NoReturn:

        self._oversample = rate

    @property
    def field_range(self) -> int:
        """Field ranges of the magnetic sensor can be selected through the register RNG.
        The full scale field range is determined by the application environments.
        For magnetic clear environment, low field range such as +/- 2gauss
        can be used. The field range goes hand in hand with the sensitivity of the
        magnetic sensor. The lowest field range has the highest sensitivity, therefore,
        higher resolution.

        Two field range values can be selected, 2G and 8G. With the following
        global variables.

        +----------------------------------------+-------------------------+
        | Mode                                   | Value                   |
        +========================================+=========================+
        | :py:const:`qmc5883.FIELDRANGE_2G`      | :py:const:`0b00`        |
        +----------------------------------------+-------------------------+
        | :py:const:`qmc5883.FIELDRANGE_8G`      | :py:const:`0b01`        |
        +----------------------------------------+-------------------------+


        Example
        ---------------------

        .. code-block:: python

            i2c = board.I2C()
            qmc = qmc5883.QMC5883L(i2c)


            qmc.field_range = qmc5883.FIELDRANGE_2G

        """

        return self._field_range

    @field_range.setter
    def field_range(self, field_range: int) -> NoReturn:

        if range == 1:
            self.resolution = 3000
        else:
            self.resolution = 12000

        self._field_range = field_range

    @property
    def output_data_rate(self) -> int:
        """Output data rate is controlled by ODR registers. Four data update
        frequencies can be selected: 10Hz, 50Hz, 100Hz and 200Hz.
        For most compassing applications, 10 Hz for low
        power consumption is recommended. For gaming, the high update rate such as
        100Hz or 200Hz can be used.


        Four oversample ratios can be selected, 10, 50, 100 or 200. With the following
        global variables.

        +-------------------------------------------+-------------------------+
        | Mode                                      | Value                   |
        +===========================================+=========================+
        | :py:const:`qmc5883.OUTPUT_DATA_RATE_10`   | :py:const:`0b00`        |
        +-------------------------------------------+-------------------------+
        | :py:const:`qmc5883.OUTPUT_DATA_RATE_50`   | :py:const:`0b01`        |
        +-------------------------------------------+-------------------------+
        | :py:const:`qmc5883.OUTPUT_DATA_RATE_100`  | :py:const:`0b10`        |
        +-------------------------------------------+-------------------------+
        | :py:const:`qmc5883.OUTPUT_DATA_RATE_200`  | :py:const:`0b11`        |
        +-------------------------------------------+-------------------------+


        Example
        ---------------------

        .. code-block:: python

            i2c = board.I2C()
            qmc = qmc5883.QMC5883L(i2c)


            qmc.output_data_rate = qmc5883.OUTPUT_DATA_RATE_200

        """

        return self._output_data_rate

    @output_data_rate.setter
    def output_data_rate(self, rate: int) -> NoReturn:

        self._output_data_rate = rate

    @property
    def mode_control(self) -> int:
        """Two bits of MODE registers can transfer mode of operations in the device,
        the two modes are Standby, and Continuous measurements. The default mode
        after Power-on-Reset (POR) is standby. There is no any restriction
        in the transferring between the modes.

        Two modes can be selected Standby and Continuous With the following
        global variables.

        +-------------------------------------------+-------------------------+
        | Mode                                      | Value                   |
        +===========================================+=========================+
        | :py:const:`qmc5883.MODE_CONTINUOUS`       | :py:const:`0b01`        |
        +-------------------------------------------+-------------------------+
        | :py:const:`qmc5883.MODE_STANDBY`          | :py:const:`0b00`        |
        +-------------------------------------------+-------------------------+


        Example
        ---------------------

        .. code-block:: python

            i2c = board.I2C()
            qmc = qmc5883.QMC5883L(i2c)


            qmc.output_data_rate = qmc5883.MODE_STANDBY

        """

        return self._mode_control

    @mode_control.setter
    def mode_control(self, mode: int) -> NoReturn:

        self._mode_control = mode

    @property
    def magnetic(self):
        """Magnetic property"""
        if self._data_ready_register == 1:

            values = (
                self._x_LSB,
                self._x_MSB,
                self._y_LSB,
                self._y_MSB,
                self._z_LSB,
                self._z_MSB,
            )

            return (
                values[0] / self.resolution,
                values[2] / self.resolution,
                values[4] / self.resolution,
            )
        return None
