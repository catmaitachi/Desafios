def verificador_de_palindromo( palavra ):
    
    """
    
    **Verificador de Palíndromos**: Verifica se uma palavra é um palíndromo *(é igual se lida de trás para frente)*.

    **Funcionamento**:

    - Converte a palavra para minúsculas para garantir que a verificação seja case-insensitive.
    - Inverte a palavra utilizando slicing.
    - Retorna um comparativo entre a palavra original e a palavra invertida.
    
    :param palavra: (str) palavra a ser verificada
    :return: (bool) true se for palíndromo, false caso contrário.
    
    """

    palavra = palavra.lower()
    palavra_invertida = palavra[::-1]

    return palavra == palavra_invertida

def main():

    palavras_teste = [ "Arara" , "Ovo" , "Casa" , "Biscoito" , "Scooby" ]

    for palavra in palavras_teste:

        if verificador_de_palindromo( palavra ): print( f'"{palavra}" é um palíndromo.' )

        else: print( f'"{palavra}" não é um palíndromo.' )

    return None

if __name__ == "__main__": main()