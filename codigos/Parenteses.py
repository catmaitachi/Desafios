def validacao_de_parenteses( expressao: str ) -> bool:

    """

    **Validação de Parênteses**: Verifica se uma expressão contendo parênteses é válida, ou seja, todos os parênteses de abertura têm um correspondente de fechamento na ordem correta.

    **⚙️ Funcionamento**:

    - Cria um dicionário para mapear os parênteses de fechamento aos seus respectivos parênteses de abertura.
    - Inicializa uma pilha vazia para armazenar os parênteses de abertura encontrados.
    - Percorre cada caractere na expressão:
        - Se o caractere for um parêntese de abertura, adiciona-o à pilha.
        - Se for um parêntese de fechamento, verifica se a pilha está vazia ou se o topo da pilha não corresponde ao parêntese de abertura esperado. Se qualquer uma dessas condições for verdadeira, retorna False.
        - Se corresponder, remove o parêntese de abertura do topo da pilha.
    - Após percorrer toda a expressão, verifica se a pilha está vazia. Se estiver, todos os parênteses foram fechados corretamente e retorna True; caso contrário, retorna False.

    **🧠 Raciocínio**:

    Isso deu uma pequena dor de cabeça inicial, mas percebi que dá para usar uma pilha para resolver o problema. Primeiro, criei alguns pares ordenados de parênteses para comparar aberturas e fechamentos; depois disso, basta passar por cada caractere da string: se detectar um parêntese de abertura, adiciona à pilha; se detectar um parêntese de fechamento, verifica se o topo da pilha corresponde ao tipo que está fechando. Se não corresponder, a expressão é inválida; caso corresponda, remove o topo da pilha. No final, se a pilha estiver vazia, significa que todos os parênteses foram fechados corretamente; caso contrário, algum não foi fechado, tornando a expressão inválida.
    
    :param expressao: string contendo os parênteses a serem validados.
    :type expressao: str
    :return: True se a expressão for válida, False caso contrário.
    :rtype: bool

    """

    correspondencias: dict[str, str] = { ')': '(', '}': '{', ']': '[' }
    pilha: list[str] = []

    for parentese in expressao:

        if parentese in correspondencias.values(): pilha.append( parentese )

        elif parentese in correspondencias.keys():
            
            if not pilha or pilha[-1] != correspondencias[ parentese ]: return False
            
            pilha.pop()

    return len( pilha ) == 0

def main():

    expressoes_teste = [ "{[()]}", "{[(])}", "{{[[(]]}}" ]

    for expressao in expressoes_teste:

        if validacao_de_parenteses( expressao ): print( f"A expressão '{expressao}' é válida." )

        else: print( f"A expressão '{expressao}' não é válida." )

if __name__ == "__main__": main()