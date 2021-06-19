# LiconIA FRAMEWORK PARA UTILIZAÇÃO DA REGRESSÃO LINEAR MÚLTIPLA COM ALGORITMOS DE OTIMIZAÇÃO

![GitHub Release](https://img.shields.io/badge/release-v0.0.1-blue.svg)
![GitHub license](https://img.shields.io/badge/license-Proprietary-yellow.svg)

## Table of contents

[TOC]

## Requirements

- Python 3.6 or superior (`sudo apt-get install python3.6` under Linux)
- Python virtual environment (`sudo apt-get install python3.6-venv` under Linux)

## Package structure (need to update)

The initial directory structure should look like this:

## Development and Tests
### 1. Installing the package

Start by creating a new virtual environment for your project. Next, update the packages `pip` and `setuptools` to the latest version. Then install the package itself.

```bash
$ sudo apt-get install python3-tk
$ /usr/bin/python3.6 -m venv --prompt="LiconIA" venv
$ source venv/bin/activate
(LiconIA) $ pip install --upgrade setuptools pip
(LiconIA) $ pip install numpy matplotlib pandas xlrd PyQt5
(LiconIA) $ pip install xlrd==1.2.0
```

### 2. Run program

```bash
$ python gui.py
```

### 3. Qt-desing Information

Information about running the interface in qt-desing
https://pythonbasics.org/qt-designer-python/


How to start Designer
```bash
$ cd /usr/lib/x86_64-linux-gnu/qt5/bin/ && ./designer
$ ./designer
```

Information about widgets the interface in qt-desing
https://doc.qt.io/qtforpython/PySide2/QtWidgets/

Convert ui to py
```bash
pyuic5 /home/linux/helloworld.ui -o helloworld.py
```
### 4. Code checking

It is also possible to check for errors in Python code using:

use a pep8 -> pycodestyle

- Diego Solak Castanho - [diegoscastanho@gmail.com](mailto:diegoscastanho@gmail.com)
- Fernando Calixto Curi - [fercuri@gmail.com](mailto:fercuri@gmail.com)

## License

This package is released and distributed under the license [GNU GPL Version 3, 29 June 2007](https://www.gnu.org/licenses/gpl-3.0.html).
