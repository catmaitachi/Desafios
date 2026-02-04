def validacao_de_parenteses( expressao ):

    """
    Desafio Validação de Parênteses:
    - Recebe uma string contendo apenas os caracteres '(', ')', '{', '}', '[' e ']'.
    - Verifica se toda abertura de parênteses tem o fechamento correspondente na ordem correta.

    :param expressao: (str) String contendo os parênteses a serem validados.
    :return: (bool) True se a expressão for válida, False caso contrário.
    """

    correspondencias = { ')': '(', '}': '{', ']': '[' } # Mapeia os parênteses de fechamento com seus respectivos parênteses de abertura.
    pilha = [] # Cria uma pilha para armazenar os parênteses de abertura.

    for char in expressao: # Loop através de cada caractere na expressão.

        if char in correspondencias.values(): pilha.append( char ) # Se o caractere for um parêntese de abertura, adiciona à pilha.

        elif char in correspondencias.keys(): # Se for um parêntese de fechamento, verifica se há um correspondente na pilha.
            
            if not pilha or pilha[-1] != correspondencias[ char ]: return False # Se a pilha estiver vazia ou o topo não corresponder, retorna False.
            
            pilha.pop() # Caso contrário, remove o parêntese de abertura correspondente do topo da pilha.

    return len( pilha ) == 0 # Retorna True se a pilha estiver vazia, ou seja, todos os parênteses foram fechados corretamente.

def main():

    expressoes_teste = [ "{[()]}", "{[(])}", "{{[[(]]}}" ]

    for expressao in expressoes_teste: # Loop através das expressões de teste.

        if validacao_de_parenteses( expressao ): print( f"A expressão '{expressao}' é válida." ) # Saída se for válida.

        else: print( f"A expressão '{expressao}' não é válida." ) # Saída se não for válida.

    return None

if __name__ == "__main__": main()