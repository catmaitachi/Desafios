def verificador_de_palindromo( palavra ):
    
    """
    Desafio Verificador de Palíndromo: 
    - Recebe uma palavra e verifica se é um palíndromo.

    :param palavra: (str) Palavra a ser verificada.
    :return: (bool) True se for palíndromo, False caso contrário.
    """

    palavra = palavra.lower() # Converte a palavra para minúsculas para garantir a comparação sem case sensitivity.
    palavra_invertida = palavra[::-1] # Inverte a palavra usando slicing.

    return palavra == palavra_invertida # Compara a palavra original com a invertida para ver se são iguais.

def main():

    palavras_teste = [ "Arara" , "Ovo" , "Casa" , "Biscoito" , "Scooby" ] # Lista de palavras para serem testadas.

    for palavra in palavras_teste: # Loop através da lista de palavras.

        if verificador_de_palindromo( palavra ): print( f'"{palavra}" é um palíndromo.' ) # Saída se for palíndromo.

        else: print( f'"{palavra}" não é um palíndromo.' ) # Saída se não for palíndromo.

    return None

if __name__ == "__main__": main()