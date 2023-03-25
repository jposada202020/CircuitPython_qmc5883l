Introduction
============

.. image:: https://readthedocs.org/projects/circuitpython-qmc5883l/badge/?version=latest
    :target: https://circuitpython-qmc5883l.readthedocs.io/
    :alt: Documentation Status

.. image:: https://github.com/jposada202020/CircuitPython_qmc5883l/workflows/Build%20CI/badge.svg
    :target: https://github.com/jposada202020/CircuitPython_qmc5883l/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

CircuitPython driver for the qmc5883l magnetometer


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_
* `Register <https://github.com/adafruit/Adafruit_CircuitPython_Register>`_

Please ensure all dependencies are available on the CircuitPython filesystem.

=====================


On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/circuitpython-qmc5883l/>`_.
To install for current user:

.. code-block:: shell

    pip3 install circuitpython-qmc5883l

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install circuitpython-qmc5883l

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install circuitpython-qmc5883l

Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install qmc5883l

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

Take a look a the ``qmc5883l_simpletest.py`` in the examples directory

Documentation
=============
API documentation for this library can be found on `Read the Docs <https://circuitpython-qmc5883l.readthedocs.io/>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/jposada202020/CircuitPython_qmc5883l/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
