def manipulacao_de_dados( lista ):

    """
    Agrupa os dados presentes em uma lista de objetos com atributos "categoria" e "valor".

    :param lista: (list) lista de objetos
    :return dados_agrupados: (obj) dados agrupados em um objeto
    """

    dados_agrupados = {} 

    for item in lista:

        categoria = item.categoria.lower()
        valor = item.valor

        dados_agrupados[categoria] = dados_agrupados.get(categoria, 0) + valor

    return dados_agrupados

def main():

    class Item:

        def __init__(self, categoria, valor):

            self.categoria = categoria
            self.valor = valor

    lista_teste = [ Item("Alimentação", 10), Item("Transporte", 5), Item("Alimentação", 20), Item("Lazer", 50) ]

    resultado = manipulacao_de_dados( lista_teste )

    print( f"Dados agrupados: {resultado}" )

    return None

if __name__ == "__main__": main()