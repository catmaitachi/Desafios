```

  ___                __ _       ___       _      __   ___          
 |   \ ___ ___ __ _ / _(_)___  |   \ __ _| |_ __ \ \ / (_)_ ____ _ 
 | |) / -_|_-</ _` |  _| / _ \ | |) / _` |  _/ _` \ V /| \ V / _` |
 |___/\___/__/\__,_|_| |_\___/ |___/\__,_|\__\__,_|\_/ |_|\_/\__,_| by Catmaitachi
                                                                   
```

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.13%2B-000000?logo=python&logoColor=white" alt="Python 3.13+ Badge"/>
</p>

## 👀 Visão Geral

Este repositório contém uma coleção de desafios de programação resolvidos em Python, feita como parte de um desafio técnico para ingressar na Bolsa de Pesquisa da [DataViva](https://www.dataviva.info/).

## 🪄 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/catmaitachi/Desafio_DataViva.git
```

2. Instale o Python:

* Na [Microsoft Store](https://apps.microsoft.com/detail/9pnrbtzxmb4z?hl=pt-BR&gl=BR).
* Ou em [python.org](https://www.python.org/downloads/). 

3. Execute os desafios na pasta `codigos/`:

```bash
cd ./Desafio_DataViva/codigos/

python FizzBuzz.py
python Palindromos.py
python Duplicados.py
python Parenteses.py
python Bonus.py
```

## 💡 Ideias, Decisões e Opiniões

Para cada desafio descrito abaixo, é possível encontrar um arquivo Python correspondente na pasta `codigos/`, linkado ao título.

Por fins de documentação e clareza, cada arquivo contém, nas respectivas funções, uma *docstring* que as torna autoexplicativas, com os seguintes detalhes:

* Uma breve descrição do desafio resolvido.
* O funcionamento do código, passo a passo.
* O raciocínio utilizado ao longo do desenvolvimento.

> "Adorei documentar nesse padrão. Ainda é possível adicionar à docstring seções como 'exemplos' e 'observações', o que pode ser bem útil dependendo do ambiente ou da equipe de desenvolvimento."

Para garantir maior robustez às funções, foi adicionada tipagem Python, oferecendo assim uma *blindagem* contra entradas indevidas.

Ademais, tentei ao máximo seguir práticas de [código limpo](https://share.google/SMLc9UAp8RuZ66eDo) ao longo do desenvolvimento e das refatorações que fui realizando, buscando deixar perceptível:

* Clareza nos nomes de variáveis e funções.
* Algoritmos simples aos olhos.
* Funções diretas e eficientes.

> "Queria fazer uma rápida menção aos esforços para aplicar os princípios SOLID; contudo, na minha visão, o escopo do desafio permite apenas exercitar alguns, como SRP e OCP."

## 🧩 Os Desafios

### 1. [O Clássico FizzBuzz](codigos/FizzBuzz.py)
Escreva um programa que imprima os números de 1 a 100.
* Para múltiplos de **3**, imprima `Fizz` em vez do número.
* Para múltiplos de **5**, imprima `Buzz` em vez do número.
* Para números múltiplos de **3 e 5** ao mesmo tempo, imprima `FizzBuzz`.

### 2. [Verificador de Palíndromos](codigos/Palindromos.py)
Crie uma função que receba uma palavra (string) e retorne `True` se ela for um palíndromo e `False` caso contrário.
* *Definição:* Palíndromo é uma palavra que pode ser lida da mesma forma de trás para frente.
* **Exemplos:** `"arara"` (True), `"ovo"` (True), `"casa"` (False).

### 3. [Encontrar Duplicados](codigos/Duplicados.py)
Dada uma lista de números inteiros, escreva uma função que identifique e retorne o número que aparece repetido.
* **Entrada:** `[1, 2, 3, 4, 2, 5]`
* **Saída Esperada:** `2`

### 4. [Validação de Parênteses](codigos/Parenteses.py)
Dada uma string contendo apenas os caracteres `(`, `)`, `{`, `}`, `[` e `]`, determine se a string é válida.
Uma string é válida se:
1.  Os parênteses abertos são fechados pelo mesmo tipo de parênteses.
2.  Os parênteses abertos são fechados na ordem correta.
* **Exemplos:**
    * `{[()]}` ✅ Válido
    * `{[(])}` ❌ Inválido (ordem errada)
    * `{{[[(]]}}` ❌ Inválido (falta fechar)

### 5. [Manipulação de Dados](codigos/Bonus.py)
Este desafio simula um cenário comum no DataViva: agrupar dados para visualização.
Dado um array de objetos representando transações:

```json
[
  { "categoria": "Alimentação", "valor": 10 },
  { "categoria": "Transporte", "valor": 5 },
  { "categoria": "Alimentação", "valor": 20 },
  { "categoria": "Lazer", "valor": 50 }
]
```
Escreva uma função que retorne um objeto (ou dicionário) com a soma dos valores por categoria.

* **Saída Esperada:** 

```json
{
  "Alimentação": 30,
  "Transporte": 5,
  "Lazer": 50
}
```