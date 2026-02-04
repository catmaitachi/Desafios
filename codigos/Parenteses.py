def validacao_de_parenteses( expressao ):

    """

    **Validação de Parênteses**: Verifica se uma expressão contendo parênteses é válida, ou seja, todos os parênteses de abertura têm um correspondente de fechamento na ordem correta.

    **Funcionamento**:

    - Cria um dicionário para mapear os parênteses de fechamento aos seus respectivos parênteses de abertura.
    - Inicializa uma pilha vazia para armazenar os parênteses de abertura encontrados
    - Percorre cada caractere na expressão:
        - Se o caractere for um parêntese de abertura, adiciona-o à pilha.
        - Se for um parêntese de fechamento, verifica se a pilha está vazia ou se o topo da pilha não corresponde ao parêntese de abertura esperado. Se qualquer uma dessas condições for verdadeira, retorna False.
        - Se corresponder, remove o parêntese de abertura do topo da pilha.
    - Após percorrer toda a expressão, verifica se a pilha está vazia. Se estiver, todos os parênteses foram fechados corretamente e retorna True; caso contrário, retorna False.

    :param expressao: (str) String contendo os parênteses a serem validados.
    :return: (bool) True se a expressão for válida, False caso contrário.

    """

    correspondencias = { ')': '(', '}': '{', ']': '[' }
    pilha = []

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

    return None

if __name__ == "__main__": main()