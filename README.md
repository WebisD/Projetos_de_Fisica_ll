# Projeto Fisíca Óptica

Projeto semestral da matéria de Física Óptica, ministrada no Centro Universitário FEI. Consiste em alguns programas desenvolvidos em python com o intuito de realizar alguns cálculos

## Funcionalidade - Projeto 1: Ondulatória

O programa realiza cálculos de conversões de ondas eletromagnéticas, campos magnéticos e elétricos

![image](images/p1_home.png)

**1 - Ondas eletromagnéticas** - É possível realizar dois tipos de conversão: "Conversão de λ para f" e "Conversão de f para λ".

É exibido ao usuário no primeiro tipo de conversão a frequência e o tipo de onda eletromagnética. Já no segundo é exibido além do tipo o comprimento da onda.

![image](images/p1_conversao1_oe.png)
![image](images/p1_conversao2_oe.png)

**2 - Campos Elétrico e Magnético** - É possível realizar seis tipos de cálculo: "Cálculo do campo Bm", "Cálculo do campo Em", "Número de onda", "Frequência angular", "Tipo de onda com k" e "Tipo de onda com ω".

![image](images/p1_calc1_cm.png)
![image](images/p1_calc2_cm.png)

No cálculo de número de onda e frequência angular é possível utilizar tanto a frequência como o comprimento de onda para se calcula-la. 

![image](images/p1_calc3_cm.png)
![image](images/p1_calc4_cm.png)

É possível descobrir o tipo de onda utilizando não só o k como também o ω

![image](images/p1_calc5_cm.png)
![image](images/p1_calc6_cm.png)


## Funcionalidade - Projeto 2: Polarizadores

O programa realiza cálculos de intensidade de luz entre polarizadores. Assim que inicia é possível selecionar o número de polarizadores.

![image](images/p2_home.png)

**Cálculo** - De acordo com o número de polarizadores deve-se também inserir o valor do ângulo.

![image](images/p2_calc1.png)
![image](images/p2_calc2.png)
![image](images/p2_calc3.png)

## Funcionalidade - Projeto 3: Átomo de hidrogênio

O programa realiza cálculos de energia, raio, comprimento de onda, fotons, cor emitida e  número quântico.

![image](images/p3_home.png)

### 1 - Número quântico
Com o número quântico o usuário pode calcular a energia cinética, potencial, total e o raio de sua órbita  

![image](images/p3_calc1_1.png)
![image](images/p3_calc1.png)

### 2 - Comprimento de onda
O usuário deve selecionar qual a série correspondente, bem como o número quântico, para assim calcular o comprimento e o espectro do fóton emitido

![image](images/p3_calc2.png)
![image](images/p3_calc2_1.png)
![image](images/p3_calc2_2.png)

### 3 - Verificar o fóton
Deve-se inserir o comprimento de onda e sua unidade, para saber se o fóton ira ionizar o átomo de hidrogênio ou não

![image](images/p3_calc3.png)
![image](images/p3_calc3_1.png)

## Execução

Tanto no Windows quanto no Linux a execução é feita a partir da execução da linha a seguir no terminal, ou utilizando uma IDE de sua preferência. 

Inicialmente deve-se instalar as bibliotecas necessárias:

No primeiro projeto:

```bash
python -m pip install -U pip
python -m pip install -U scipy
```

No terceiro projeto

```bash
python -m pip install --upgrade pip wheel setuptools virtualenv
python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*
python -m pip install kivy_deps.gstreamer==0.1.*
python -m pip install kivy[base] kivy_examples --pre --extra-index-url https://kivy.org/downloads/simple/
```

```bash
python main.py
```

Entretanto, utilizando apenas a linha acima é possivel que o compilador de sua máquina utilize o python em sua versão 2.7. Para resolver isso é mais vantajoso utilizar:

```bash
python3 main.py
```

Caso você esteja utilizando o Windows é possível executar o projeto apenas executando o arquivo "clickme.exe.bat"