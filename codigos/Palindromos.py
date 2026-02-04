def verificador_de_palindromo( palavra: str ) -> bool:
    
    """
    
    **Verificador de Palíndromos**: Verifica se uma palavra é um palíndromo *(é igual se lida de trás para frente)*.

    **⚙️ Funcionamento**:

    - Converte a palavra para minúsculas para garantir que a verificação seja case-insensitive.
    - Inverte a palavra utilizando slicing.
    - Retorna um comparativo entre a palavra original e a palavra invertida.

    **🧠 Raciocínio**:

    Pensando em formas de verificar se uma palavra é um palíndromo, a abordagem mais direta é comparar a palavra original com a sua versão invertida. Em Python, é possível inverter uma string usando slicing (`palavra[::-1]`), o que torna tudo bem simples. Por fim, usei `palavra.lower()` para garantir que a comparação não seja sensível a maiúsculas/minúsculas; depois foi só retornar o resultado booleano.
    
    :param palavra: (str) palavra a ser verificada
    :return: (bool) True se for palíndromo, False caso contrário.
    
    """

    palavra = palavra.lower()
    palavra_invertida = palavra[::-1]

    return palavra == palavra_invertida

def main():

    palavras_teste = [ "Arara" , "Ovo" , "Casa" , "Biscoito" , "Scooby" ]

    for palavra in palavras_teste:

        if verificador_de_palindromo( palavra ): print( f'"{palavra}" é um palíndromo.' )

        else: print( f'"{palavra}" não é um palíndromo.' )

if __name__ == "__main__": main()