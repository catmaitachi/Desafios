def encontrar_duplicados( lista ):

    """
    
    **Encontrar Duplicados**: Faz uma varredura em uma lista de inteiros à procura de números duplicados.

    **Funcionamento**:

    - Cria um conjunto para armazenar os números já verificados.
    - Cria uma lista para armazenar os números duplicados encontrados.
    - Percorre cada número na lista fornecida:
        - Se o número já estiver no conjunto de verificados e não estiver na lista de duplicados, adiciona-o à lista de duplicados.
        - Caso contrário, adiciona o número ao conjunto de verificados.
    - Retorna a lista de números duplicados encontrados.

    :param lista: (list) lista de números inteiros
    :return duplicados: (list) lista de números duplicados
    
    """

    verificados = set()
    duplicados  = []

    for numero in lista: 

        if numero in verificados and numero not in duplicados: duplicados.append( numero )

        else: verificados.add( numero )

    return duplicados

def main():

    lista_teste = [ 1, 2, 3, 4, 2, 5 ]

    duplicados_encontrados = encontrar_duplicados( lista_teste )

    print( f"Números duplicados encontrados: {duplicados_encontrados}" )

    return None

if __name__ == "__main__": main()