def calcular_bits_paridade(mensagem, num_linhas, num_colunas):
    matriz = [[int(mensagem[i * num_colunas + j]) for j in range(num_colunas)] for i in range(num_linhas)]

    # Calcular bits de paridade das linhas
    paridade_linhas = [str(sum(matriz[i]) % 2) for i in range(num_linhas)]

    # Calcular bits de paridade das colunas
    paridade_colunas = [str(sum(matriz[i][j] for i in range(num_linhas)) % 2) for j in range(num_colunas)]

    # Retornar os bits de paridade em ordem
    return ''.join(paridade_linhas + paridade_colunas)

def decodificar_mensagem(mensagem_codificada, bits_paridade, num_linhas, num_colunas):
    # Verifica a paridade das linhas
    for i in range(num_linhas):
        paridade_linha = sum(map(int, mensagem_codificada[i * num_colunas : (i + 1) * num_colunas])) % 2
        if paridade_linha != int(bits_paridade[i]):
            print(f"Erro na linha {i + 1}")

    # Verifica a paridade das colunas
    for j in range(num_colunas):
        valores_coluna = [int(mensagem_codificada[i * num_colunas + j]) for i in range(num_linhas)]
        paridade_coluna = sum(valores_coluna) % 2
        if paridade_coluna != int(bits_paridade[num_linhas + j]):
            print(f"Erro na coluna {j + 1}")

    # Reconstrói a mensagem original excluindo os bits de paridade
    mensagem_original = ''.join([mensagem_codificada[i * num_colunas : (i + 1) * num_colunas] for i in range(num_linhas)])
    return mensagem_original


mensagem = input("Digite a mensagem: ")
num_linhas = int(input("Digite o número de linhas: "))
num_colunas = int(input("Digite o número de colunas: "))

opcao = int(input("Selecione uma opção:\n\n1 - Calcular bits de paridade\n2 - Descobrir mensagem original (sem bits de paridade)"))

if opcao == 1:

    bits_paridade = calcular_bits_paridade(mensagem, num_linhas, num_colunas)
    print("Bits de paridade: ", bits_paridade)

elif opcao == 2:
    bits_paridade = input("Digite os bits de paridade (em ordem, primeiro linha, depois coluna): ")
    mensagem_original = decodificar_mensagem(mensagem, bits_paridade, num_linhas, num_colunas)
    print("A mensagem original é:", mensagem_original)
