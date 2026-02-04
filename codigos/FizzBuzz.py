def fizzbuzz( incio , fim ):
    
    """
    Desafio FizzBuzz: 
    - Imprima os números dentro de um intervalo.
    - Para múltiplos de 3, imprima "Fizz".
    - Para múltiplos de 5, imprima "Buzz".
    - Para múltiplos de ambos 3 e 5, imprima "FizzBuzz".

    :param incio: (int) incio do intervalo 
    :param fim: (int) final do intervalo
    """

    for i in range( incio, fim + 1 ): # Cria um loop no intervalo definido.

        if i % 3 == 0 and i % 5 == 0: print( str(i) + " - FizzBuzz" ) # Verifica se o número é múltiplo de 3 e 5 ao mesmo tempo para imprimir "FizzBuzz".

        elif i % 3 == 0: print( str(i) + " - Fizz" ) # Verifica se o número é múltiplo de 3 para imprimir "Fizz".

        elif i % 5 == 0: print( str(i) + " - Buzz" ) # Verifica se o número é múltiplo de 5 para imprimir "Buzz".

        else: print( str(i) ) # Imprime o número sem nada caso não seja múltiplo de 3 ou 5.

    # ! Obs: Deixei a função sem validação de parâmetros para manter o foco no desafio proposto.

    return None

def main():
    
    fizzbuzz( 1, 100 ) # Chama a função com o intervalo de 1 a 100.

    return None

if __name__ == "__main__": main()