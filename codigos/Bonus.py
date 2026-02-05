from typing import List

class Item():

    def __init__(self, categoria: str, valor: float | int):

        self.categoria = categoria
        self.valor = valor

def manipulacao_de_dados( lista: List[Item] ) -> dict[str, float | int]:

    """

    **Manipulação de Dados**: Agrupa uma lista de objetos por uma propriedade "*categoria*" e calcula a soma de outra propriedade "*valor*" para cada grupo.

    **⚙️ Funcionamento**:

    - Cria um dicionário vazio para armazenar os dados agrupados.
    - Percorre cada objeto na lista fornecida:
        - Extrai a categoria e o valor do objeto.
        - Adiciona o valor à soma correspondente à categoria no dicionário.

    **🧠 Raciocínio**:

    Eu acabei pensando em duas ou três formas de construir essa função, algumas um tanto complexas, mas percebi que era possível fazer isso com um código bem mais simples. Eu criei a classe `Item` para exemplificar a função, mas ela em si é genérica e pode ser aplicada a qualquer lista de objetos que tenham as propriedades "*categoria*" e "*valor*". Ela percorre a lista, catalogando as categorias e somando os valores correspondentes, criando assim um dicionário que representa a lista de objetos agrupada por categoria.

    :param lista: lista de objetos.
    :type lista: List[Item]
    :return: dados agrupados em um dicionário.
    :rtype: dict[str, float | int]

    """

    dicionario: dict[str, float | int] = {} 

    for item in lista:

        categoria = item.categoria.lower()
        valor = item.valor

        dicionario[categoria] = dicionario.get(categoria, 0) + valor

    return dicionario

def main():

    lista_teste = [ Item("Alimentação", 10), Item("Transporte", 5), Item("Alimentação", 20), Item("Lazer", 50) ]

    resultado = manipulacao_de_dados( lista_teste )

    print( f"Dados agrupados: {resultado}" )

if __name__ == "__main__": main()