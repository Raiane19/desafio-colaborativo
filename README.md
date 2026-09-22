# 🌡️ Conversor de Temperatura

Projeto desenvolvido em **Python** com o objetivo de realizar conversões entre diferentes escalas de temperatura.

O programa permite converter valores entre **Celsius, Fahrenheit e Kelvin**, utilizando um menu interativo no terminal.

---

## 📌 Objetivo

O objetivo deste projeto é desenvolver um conversor de temperaturas simples e funcional, aplicando conceitos fundamentais de programação em Python, como:

* Funções;
* Variáveis;
* Entrada e saída de dados;
* Estruturas condicionais;
* Laço de repetição `while`;
* Operações matemáticas;
* Organização de código.

O projeto também foi desenvolvido de forma **colaborativa**, permitindo que diferentes integrantes trabalhassem em partes específicas do programa por meio de branches no Git.

---

## 🌡️ Conversões disponíveis

O programa possui **6 tipos de conversão**:

| Opção | Conversão            |
| ----- | -------------------- |
| 1     | Celsius → Fahrenheit |
| 2     | Fahrenheit → Celsius |
| 3     | Celsius → Kelvin     |
| 4     | Kelvin → Celsius     |
| 5     | Fahrenheit → Kelvin  |
| 6     | Kelvin → Fahrenheit  |

Além disso, a opção `0` encerra o programa.

---

## 🧮 Fórmulas utilizadas

### Celsius → Fahrenheit

```text
°F = (°C × 9/5) + 32
```

### Fahrenheit → Celsius

```text
°C = (°F - 32) × 5/9
```

### Celsius → Kelvin

```text
K = °C + 273.15
```

### Kelvin → Celsius

```text
°C = K - 273.15
```

### Fahrenheit → Kelvin

```text
K = (°F - 32) × 5/9 + 273.15
```

### Kelvin → Fahrenheit

```text
°F = (K - 273.15) × 9/5 + 32
```

---

## ⚙️ Funcionamento

Ao executar o programa, será apresentado um menu com todas as opções de conversão:

```text
================================
     CONVERSOR DE TEMPERATURA
================================

1 - Celsius → Fahrenheit
2 - Fahrenheit → Celsius
3 - Celsius → Kelvin
4 - Kelvin → Celsius
5 - Fahrenheit → Kelvin
6 - Kelvin → Fahrenheit
0 - Sair
```

O usuário escolhe uma opção e informa o valor da temperatura.

O programa realiza o cálculo correspondente e apresenta o resultado com **duas casas decimais**.

Após a conversão, o menu é apresentado novamente, permitindo realizar outras conversões.

O programa permanece funcionando até que o usuário escolha a opção `0`.

---

## 🧩 Estrutura das funções

Cada conversão foi implementada por meio de uma função específica.

### Celsius → Kelvin

```python
def celsius_para_kelvin(celsius):
    return celsius + 273.15
```

### Kelvin → Celsius

```python
def kelvin_para_celsius(kelvin):
    return kelvin - 273.15
```

O uso de funções permite separar cada operação e deixar o código mais organizado e fácil de entender.

---

## 🔄 Estrutura do programa

O funcionamento geral pode ser representado da seguinte forma:

```text
Início
  ↓
Exibe o menu
  ↓
Usuário escolhe uma opção
  ↓
Identifica a conversão
  ↓
Solicita a temperatura
  ↓
Realiza o cálculo
  ↓
Exibe o resultado
  ↓
Volta para o menu
  ↓
Usuário escolhe 0?
  ├── Não → Continua o programa
  └── Sim → Encerra
```

---

## 👥 Desenvolvimento colaborativo

O projeto foi desenvolvido de maneira colaborativa utilizando **Git e GitHub**.

Cada integrante ficou responsável por um conjunto de conversões:

### 👤 Raiane dos Santos

**Celsius ↔ Fahrenheit**

Funções:

```python
celsius_para_fahrenheit()
fahrenheit_para_celsius()
```

### 👤 Nilton Alves

**Celsius ↔ Kelvin**

Funções:

```python
celsius_para_kelvin()
kelvin_para_celsius()
```

### 👤 Arthur Ribeiro

**Fahrenheit ↔ Kelvin**

Funções:

```python
fahrenheit_para_kelvin()
kelvin_para_fahrenheit()
```

O uso de **branches** permite que cada integrante desenvolva sua parte sem alterar diretamente a branch principal do projeto.

---

## 🛠️ Tecnologias utilizadas

* **Python**
* **Git**
* **GitHub**
* **Git Bash**

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Entre na pasta do projeto

```bash
cd nome-do-repositorio
```

### 3. Execute o programa

```bash
python conversor.py
```

Caso seu sistema utilize o comando `python3`:

```bash
python3 conversor.py
```

---

## 📚 Conceitos de programação aplicados

Este projeto utiliza conceitos importantes para o aprendizado de Python:

* **Funções (`def`)** para organizar as conversões;
* **`return`** para retornar os resultados dos cálculos;
* **`input()`** para receber informações do usuário;
* **`float()`** para trabalhar com valores decimais;
* **`if/elif/else`** para verificar a opção escolhida;
* **`while`** para manter o programa funcionando;
* **`break`** para encerrar o programa;
* **f-strings** para apresentar os resultados;
* **Operadores matemáticos** para realizar as conversões.

---

## 🎯 Exemplo de execução

```text
================================
     CONVERSOR DE TEMPERATURA
================================

1 - Celsius → Fahrenheit
2 - Fahrenheit → Celsius
3 - Celsius → Kelvin
4 - Kelvin → Celsius
5 - Fahrenheit → Kelvin
6 - Kelvin → Fahrenheit
0 - Sair

Escolha uma opção: 3

Digite a temperatura em Celsius: 25

Resultado: 298.15 K
```

---

## 🚀 Possíveis melhorias

O projeto pode ser expandido futuramente com funcionalidades como:

* Validação dos valores informados;
* Tratamento de entradas inválidas;
* Interface gráfica;
* Histórico das conversões;
* Mais escalas de temperatura;
* Testes automatizados;
* Separação do projeto em diferentes arquivos Python.

---

## 📄 Licença

Este projeto foi desenvolvido para fins **educacionais e acadêmicos**.
