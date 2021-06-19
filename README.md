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
O programa realiza cálculos de conversões de ondas eletromagnéticas, campos magnéticos e elétricos

![app](https://github.com/antuniooh/optical-physics-simulator/blob/master/images/app.gif)

1 - Ondas eletromagnéticas - É possível realizar dois tipos de conversão: "Conversão de λ para f" e "Conversão de f para λ".

É exibido ao usuário no primeiro tipo de conversão a frequência e o tipo de onda eletromagnética. Já no segundo é exibido além do tipo o comprimento da onda

2 - Campos Elétrico e Magnético - É possível realizar seis tipos de cálculo: "Cálculo do campo Bm", "Cálculo do campo Em", "Número de onda", "Frequência angular", "Tipo de onda com k" e "Tipo de onda com ω".

No cálculo de número de onda e frequência angular é possível utilizar tanto a frequência como o comprimento de onda para se calcula-la.

É possível descobrir o tipo de onda utilizando não só o k como também o ω

# Project 2 - Polarizers
O programa realiza cálculos de intensidade de luz entre polarizadores. Assim que inicia é possível selecionar o número de polarizadores.

Cálculo - De acordo com o número de polarizadores deve-se também inserir o valor do ângulo.

![app](https://github.com/antuniooh/optical-physics-simulator/blob/master/images/app.gif)

# Project 3 - Hydrogen Atom
O programa realiza cálculos de energia, raio, comprimento de onda, fotons, cor emitida e número quântico.

1 - Número quântico: Com o número quântico o usuário pode calcular a energia cinética, potencial, total e o raio de sua órbita

2 - Comprimento de onda: O usuário deve selecionar qual a série correspondente, bem como o número quântico, para assim calcular o comprimento e o espectro do fóton emitido

3 - Verificar o fóton: Deve-se inserir o comprimento de onda e sua unidade, para saber se o fóton ira ionizar o átomo de hidrogênio ou não

![app](https://github.com/antuniooh/optical-physics-simulator/blob/master/images/app.gif)

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
