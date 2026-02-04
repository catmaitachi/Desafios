def manipulacao_de_dados( lista ):

    """

    **Manipulação de Dados**: Agrupa uma lista de objetos por uma propriedade "*categoria*" e calcula a soma de outra propriedade "*valor*" para cada grupo.

    **Funcionamento**:

    - Cria um dicionário vazio para armazenar os dados agrupados.
    - Percorre cada objeto na lista fornecida:
        - Extrai a categoria e o valor do objeto.
        - Adiciona o valor à soma correspondente à categoria no dicionário.

    :param lista: (list) lista de objetos
    :return dicionario: (dict) dados agrupados em um dicionário

    """

    dicionario = {} 

    for item in lista:

        categoria = item.categoria.lower()
        valor = item.valor

        dicionario[categoria] = dicionario.get(categoria, 0) + valor

    return dicionario

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