def calcular_bits_paridade(mensagem, num_linhas, num_colunas):
    matriz = [[int(mensagem[i * num_colunas + j]) for j in range(num_colunas)] for i in range(num_linhas)]

    # Calcular bits de paridade das linhas
    paridade_linhas = [str(sum(matriz[i]) % 2) for i in range(num_linhas)]

    # Calcular bits de paridade das colunas
    paridade_colunas = [str(sum(matriz[i][j] for i in range(num_linhas)) % 2) for j in range(num_colunas)]

    # Retornar os bits de paridade em ordem
    return ''.join(paridade_linhas + paridade_colunas)

def decodificar_mensagem(mensagem, num_linhas, num_colunas):
    mensagem_original = ""

    # Remover bits de paridade das linhas
    bits_mensagem = mensagem[:-num_linhas]
    
    # Dividir a mensagem em blocos de acordo com o número de colunas
    blocos = [bits_mensagem[i:i+num_colunas] for i in range(0, len(bits_mensagem), num_colunas)]

    # Transpor a matriz para decodificar a mensagem original
    matriz_transposta = [list(x) for x in zip(*blocos)]

    for linha in matriz_transposta:
        mensagem_original += ''.join(linha)

    return mensagem_original


mensagem = input("Digite a mensagem: ")
num_linhas = int(input("Digite o número de linhas: "))
num_colunas = int(input("Digite o número de colunas: "))

opcao = int(input("Selecione uma opção:\n\n1 - Calcular bits de paridade\n2 - Descobrir mensagem original (sem bits de paridade)"))

if opcao == 1:

    bits_paridade = calcular_bits_paridade(mensagem, num_linhas, num_colunas)
    print("Bits de paridade: ", bits_paridade)

elif opcao == 2:

    mensagem_original = decodificar_mensagem(mensagem, num_linhas, num_colunas)
    print("A mensagem original é:", mensagem_original)
