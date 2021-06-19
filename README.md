# LiconIA
## Framework that uses artificial intelligence applied to mathematical models to make predictions

![GitHub Release](https://img.shields.io/badge/release-v0.0.1-blue.svg)
![GitHub license](https://img.shields.io/badge/license-Proprietary-yellow.svg)

----
## Interface Overview    

![image](https://github.com/diegoscastanho/LiconIA/blob/main/images/intarface.png?raw=true)

## Table of contents

[TOC]

<br>

## 1 Articles, theses for technical support
### 1.1 Final Coursework
-----
- [Analyses of genetic algorithms and differential evolution for non-linear multimodal functions optimization](http://repositorio.utfpr.edu.br/jspui/handle/1/16249)
- [Swarm intelligence algorithms for binary optmization](http://repositorio.utfpr.edu.br/jspui/handle/1/16251)


<br>

### 1.2 Dissertation
-----
- [Predicting the state of charge of the battery applied to electric vehicles using linear models self-tuned through optimization algorithms](http://repositorio.utfpr.edu.br/jspui/handle/1/4758)
- [Ensembled method based on artificial neural networks for the estimation of respiratory diseases](https://repositorio.utfpr.edu.br/jspui/handle/1/4038)
- [Gaussian Adaptive PID control with robust parameters considering plant parameter variation with optimization based on bioinspired metaheuristics](http://repositorio.utfpr.edu.br/jspui/handle/1/4880)
- [Prediction of affluent flows using artificial neural networks and ensembles](http://repositorio.utfpr.edu.br/jspui/handle/1/4037)
- [Analysis of data clustering methods to detect anomalies in the pricing and categorization of automotive industry parts](http://repositorio.utfpr.edu.br/jspui/handle/1/24489)

<br>

### 1.3 Theses 
-----
loading...


<br>

### 1.4 Articles
----
- [Air pollution epidemiology: A simplified Generalized Linear Model approach optimized by bio-inspired metaheuristics](https://www.sciencedirect.com/science/article/abs/pii/S0013935120310033)

<br>

## 2 Requirements
---
- Python 3.6 or superior (`sudo apt-get install python3.6` under Linux)
- Python virtual environment (`sudo apt-get install python3.6-venv` under Linux)

<br>

## 3 Package structure (need to update)
----

The initial directory structure should look like this:

<br>

## 4 Development and Tests
### 4.1 Installing the package
---

Start by creating a new virtual environment for your project. Next, update the packages `pip` and `setuptools` to the latest version. Then install the package itself.

```bash
$ sudo apt-get install python3-tk
$ /usr/bin/python3.6 -m venv --prompt="LiconIA" venv
$ source venv/bin/activate
(LiconIA) $ pip install --upgrade setuptools pip
(LiconIA) $ pip install numpy matplotlib pandas xlrd PyQt5
(LiconIA) $ pip install xlrd==1.2.0
```

<br>

### 4.2 Run program
---
To run the code just type:

```bash
$ python run.py
```

<br>

### 4.3 Qt-desing Information
----

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

<br>

### 4.4 Code checking
-----
It is also possible to check for errors in Python code using:

use a pep8 -> pycodestyle

<br>

### 4.5 Development Team
-----
- Diego Solak Castanho - [diegoscastanho@gmail.com](mailto:diegoscastanho@gmail.com)
- Fernando Calixto Curi - [fercuri@gmail.com](mailto:fercuri@gmail.com)

<br>

## 5 License
-----

This package is released and distributed under the license [GNU GPL Version 3, 29 June 2007](https://www.gnu.org/licenses/gpl-3.0.html).
