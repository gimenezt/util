def calcular_bits_paridade(mensagem, num_linhas, num_colunas):
    matriz = [[int(mensagem[i * num_colunas + j]) for j in range(num_colunas)] for i in range(num_linhas)]

    # Calcular bits de paridade das linhas
    paridade_linhas = [str(sum(matriz[i]) % 2) for i in range(num_linhas)]

    # Calcular bits de paridade das colunas
    paridade_colunas = [str(sum(matriz[i][j] for i in range(num_linhas)) % 2) for j in range(num_colunas)]

    # Retornar os bits de paridade em ordem
    return ''.join(paridade_linhas + paridade_colunas)

mensagem = input("Digite a mensagem binária: ")
num_linhas = int(input("Digite o número de linhas: "))
num_colunas = int(input("Digite o número de colunas: "))

bits_paridade = calcular_bits_paridade(mensagem, num_linhas, num_colunas)
print("Bits de paridade: ", bits_paridade)
