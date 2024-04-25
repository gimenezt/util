import math

def calcular_media(dados):
    return sum(dados) / len(dados)

def calcular_desvio_padrao_media(dados):
    media = calcular_media(dados)
    somatorio = sum([(x - media) ** 2 for x in dados])
    desvio_padrao = math.sqrt(somatorio / (len(dados) * (len(dados) - 1)))
    return desvio_padrao

def main():
    try:
        num_dados = int(input("Quantos dados você tem? "))
        dados = []
        for i in range(num_dados):
            dado = float(input(f"Insira o dado {i+1}: "))
            dados.append(dado)
        
        media = calcular_media(dados)
        print("A média dos dados é:", media)
        
        desvio_padrao_media = calcular_desvio_padrao_media(dados)
        print("O desvio padrão da média é:", desvio_padrao_media)
        
    except ValueError:
        print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()