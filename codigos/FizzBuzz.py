def fizzbuzz( numero: int ) -> str | None:
    
    """

    **FizzBuzz**: Analisa um número e retorna "Fizz" se for múltiplo de 3, "Buzz" se for múltiplo de 5 e "FizzBuzz" se for múltiplo de ambos. Se não for múltiplo de nenhum, retorna None.

    **⚙️ Funcionamento**:
    
    - Para cada número:
        - Verifica se é múltiplo de 3 e 5, retornando "FizzBuzz" se verdadeiro.
        - Verifica se é múltiplo de 3, retornando "Fizz" se verdadeiro.
        - Verifica se é múltiplo de 5, retornando "Buzz" se verdadeiro.
        - Se não for múltiplo de nenhum, retorna None.

    **🧠 Raciocínio**:

    O algoritmo é simples e direto: ele deve verificar algumas condicionais a respeito do número. O mais importante é garantir a ordem correta das verificações, começando pelo caso mais específico (múltiplo de ambos) e depois os casos individuais. Se o número não atender a nenhuma das condições, retornamos None para indicar que ele não é múltiplo de 3 ou 5.

    :param numero: número a ser verificado.
    :type numero: int
    :return: "Fizz", "Buzz", "FizzBuzz" ou None
    :rtype: str | None

    """

    if numero % 3 == 0 and numero % 5 == 0: return "FizzBuzz"

    elif numero % 3 == 0: return "Fizz"

    elif numero % 5 == 0: return "Buzz"

    else: return None 

def impressora_fizzbuzz( iteracoes: int ) -> None:

    """

    **Impressora FizzBuzz**: Imprime os números de um intervalo, adicionando as palavras "Fizz", "Buzz" ou "FizzBuzz" para os múltiplos de 3, 5 ou ambos, respectivamente.

    **⚙️ Funcionamento**:

    - Inicia um loop para iterar de 1 até o número de `iterações` especificado.
        - Para cada número no intervalo:
            - Chama a função `fizzbuzz` para obter a string correspondente.
            - Imprime o número seguido da string retornada (se houver).

    **🧠 Raciocínio**:

    Funciona como uma extensão da função `fizzbuzz`, onde iteramos por um intervalo de números e para cada um, chamamos `fizzbuzz` para determinar o que deve ser impresso junto ao número.
    
    :param iteracoes: número de iterações a serem impressas.
    :type iteracoes: int

    """

    for numero in range( 1, iteracoes + 1 ):

        print( f"{numero}: {fizzbuzz(numero) or ''}" )


def main():
    
    impressora_fizzbuzz( 100 )

if __name__ == "__main__": main()