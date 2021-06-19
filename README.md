<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/antuniooh/optical-physics-simulator">

  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/antuniooh/optical-physics-simulator">
  
  <a href="https://github.com/antuniooh/optical-physics-simulator/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/antuniooh/optical-physics-simulator">
  </a>
  
   <img alt="GitHub" src="https://img.shields.io/github/license/antuniooh/optical-physics-simulator">
</p>


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/antuniooh/optical-physics-simulator">
    <img src="https://github.com/antuniooh/optical-physics-calculator/blob/master/code/Projeto%201%20-%20Ondulat%C3%B3ria/fundo.jpg" alt="Logo" width="550">
  </a>
</p>

<p align="center">
  <img alt="Math" src="https://img.shields.io/badge/Math-red?style=for-the-badge&logo=math&logoColor=white"/>
  <img alt="Python" src="https://img.shields.io/badge/Python-darkblue?style=for-the-badge&logo=python&logoColor=white"/>
    <img alt="Physics" src="https://img.shields.io/badge/Physics-darkrgreen?style=for-the-badge&logo=physics&logoColor=white"/>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#-about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#-how-to-run">How To Run</a>
    </li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## 💻 About The Project

# Project 1 - Undulatory
The program performs electromagnetic wave, magnetic and electric field conversion calculations

![app](https://github.com/antuniooh/optical-physics-simulator/blob/master/images/app1.gif)

1 - Electromagnetic waves - It is possible to carry out two types of conversion: "Conversion from λ to f" and "Conversion from f to λ".

The user is shown in the first type of conversion the frequency and type of electromagnetic wave. In the second, in addition to the type, the wavelength is displayed

2 - Electric and Magnetic Fields - It is possible to perform six types of calculation: "Bm field calculation", "Em field calculation", "Wave number", "Angular frequency", "Wave type with k" and "Type waveform with ω".

In the calculation of wavenumber and angular frequency it is possible to use both the frequency and the wavelength to calculate it.

It is possible to find the wave type using not only the k but also the ω

# Project 2 - Polarizers
The program performs light intensity calculations between polarizers. Once it starts it is possible to select the number of polarizers.

Calculation - According to the number of polarizers, the angle value must also be entered.

![app](https://github.com/antuniooh/optical-physics-simulator/blob/master/images/app2.gif)

# Project 3 - Hydrogen Atom
The program performs energy, radius, wavelength, photon, emitted color and quantum number calculations.

![app](https://github.com/antuniooh/optical-physics-simulator/blob/master/images/app3.gif)

1 - Quantum number: With the quantum number the user can calculate the kinetic, potential, total energy and the radius of its orbit

2 - Wavelength: The user must select the corresponding series, as well as the quantum number, in order to calculate the length and spectrum of the emitted photon.

3 - Check the photon: You must enter the wavelength and its unit, to know if the photon will ionize the hydrogen atom or not

<!-- HOW TO RUN -->
## 🚀 How To Run

```bash

# Clone the repository
$ git clone https://github.com/antuniooh/optical-physics-simulator.git

# Access the project folder in your terminal / cmd
$ cd optical-physics-simulator/src

# Install the libs
$ python -m pip install -U pip
$ python -m pip install -U scipy
$ python -m pip install --upgrade pip wheel setuptools virtualenv
$ python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*
$ python -m pip install kivy_deps.gstreamer==0.1.*
$ python -m pip install kivy[base] kivy_examples --pre --extra-index-url https://kivy.org/downloads/simple/

# Go to one project
$ cd <project_folder>

# In both Windows and Linux, the execution is done by executing the following line in the terminal, or using an IDE of your choice.
$ python3 main.py

```

<!-- AUTHORS -->
## 🤖 Authors

[Antonio Gustavo](https://github.com/antuniooh)           |  [Tainá Bueno](https://github.com/tainacbueno)           |  [Weverson da Silva](https://github.com/WebisD)
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://avatars.githubusercontent.com/u/51217271?v=4" alt="drawing" width="150"/>  |  <img src="https://avatars.githubusercontent.com/u/56885213?v=4" alt="drawing" width="150"/>| <img src="https://avatars.githubusercontent.com/u/49571908?v=4" alt="drawing" width="150"/>
22.119.001-0 | 22.119.006-9 | 22.119.004-4
