```

  ___                __ _       ___       _      __   ___          
 |   \ ___ ___ __ _ / _(_)___  |   \ __ _| |_ __ \ \ / (_)_ ____ _ 
 | |) / -_|_-</ _` |  _| / _ \ | |) / _` |  _/ _` \ V /| \ V / _` |
 |___/\___/__/\__,_|_| |_\___/ |___/\__,_|\__\__,_|\_/ |_|\_/\__,_| by Catmaitachi
                                                                   
```

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.11%2B-000000?logo=python&logoColor=white" alt="Python 3.11+ Badge"/>
</p>

## 👀 Visão Geral

Esse repositório contém uma coleção de desafios de programação resolvidos em Python, feito como desafio técnico para ingressar na Bolsa de Pesquisa da [DataViva](https://www.dataviva.info/). 

## 🧩 Os desafios

### 1. [O Clássico FizzBuzz](codigos/FizzBuzz.py)
Escreva um programa que imprima os números de 1 a 100.
* Para múltiplos de **3**, imprima `Fizz` em vez do número.
* Para múltiplos de **5**, imprima `Buzz` em vez do número.
* Para números múltiplos de **3 e 5** ao mesmo tempo, imprima `FizzBuzz`.

### 2. [Verificador de Palíndromos](codigos/Palindromos.py)
Crie uma função que receba uma palavra (string) e retorne `true` se ela for um palíndromo e `false` caso contrário.
* *Definição:* Palíndromo é uma palavra que pode ser lida da mesma forma de trás para frente.
* **Exemplos:** `"arara"` (true), `"ovo"` (true), `"casa"` (false).

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
Escreva uma função que retorne um objeto (ou dicionário) somando os valores por categoria.

* **Saída Esperada:** 

```json
{
  "Alimentação": 30,
  "Transporte": 5,
  "Lazer": 50
}
```