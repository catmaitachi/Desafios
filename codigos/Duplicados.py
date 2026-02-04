def encontrar_duplicados( lista ):

    """
    Desafio Encontrar Duplicados: 
    - Recebe uma lista de números inteiros.
    - Retorna os números que aparecem mais de uma vez na lista.

    :param lista: (list) lista de números inteiros
    :return duplicados: (list) lista de números duplicados
    """

    verificados = set() # Conjunto para armazenar os números já verificados.
    duplicados  = [] # Lista para armazenar os números duplicados.

    for numero in lista: 

        if numero in verificados and numero not in duplicados: duplicados.append( numero ) # Se o número aparecer novamente e não estiver na lista de duplicados, adiciona-o.

        else: verificados.add( numero ) # Adiciona o número ao conjunto de verificados.

    return duplicados # Retorna a lista de números duplicados.

def main():

    lista_teste = [ 1, 2, 3, 4, 2, 5 ] # Lista de números para teste.

    duplicados_encontrados = encontrar_duplicados( lista_teste ) # Chama a função para encontrar duplicados.

    print( f"Números duplicados encontrados: {duplicados_encontrados}" ) # Exibe os resultados.

    return None

if __name__ == "__main__": main()