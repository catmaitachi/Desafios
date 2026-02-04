def fizzbuzz( inicio, fim ):
    
    """

    **FizzBuzz**: Imprime os números de um intervalo (*inicio* a *fim*) com as seguintes regras:

    - Para múltiplos de 3, imprime "Fizz" ao lado do número.
    - Para múltiplos de 5, imprime "Buzz" ao lado do número.
    - Para múltiplos de ambos 3 e 5, imprime "FizzBuzz" ao lado do número.

    **Funcionamento**:
    
    - Cria um loop que percorre um a um os números do intervalo (*inicio* a *fim*).
        - Para cada número:
            - Verifica se é múltiplo de 3 e 5, imprimindo "FizzBuzz" se verdadeiro.
            - Verifica se é múltiplo de 3, imprimindo "Fizz" se verdadeiro.
            - Verifica se é múltiplo de 5, imprimindo "Buzz" se verdadeiro.
            - Se não for múltiplo de nenhum, apenas imprime o número.

    :param inicio: (int) inicio do intervalo 
    :param fim: (int) final do intervalo

    """

    for i in range( inicio, fim + 1 ):

        if i % 3 == 0 and i % 5 == 0: print( str(i) + " - FizzBuzz" )

        elif i % 3 == 0: print( str(i) + " - Fizz" )

        elif i % 5 == 0: print( str(i) + " - Buzz" )

        else: print( str(i) )

    return None

def main():
    
    fizzbuzz( 1, 100 )

    return None

if __name__ == "__main__": main()