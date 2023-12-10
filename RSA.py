def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    else:
        m, n, o = extended_euclidean(b % a, a)
        return m, o - (b // a) * n, n

def find_d(e, F):
    m, x, y = extended_euclidean(e, F)
    if m != 1:
        raise ValueError(f"{e} is not invertible module {F}")
    else:
        return x % F

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def find_coprime(F):
    for e in range(2, F):
        if gcd(e, F) == 1:
            return e
    return None

def calculate_F_p_q(p, q):
    return lcm(p - 1, q - 1)

def menu_calculate_d():
    option = int(input("Se você não tem o valor de e, primeiro calcule-o. Cancele o script e volte. \nVocê tem:\n1 - Valores de p e q\n2 - Valor de F\n"))

    if option == 1:
        e = int(input("Insira o valor de e: "))
        F = int(input("Insira o valor de F: "))

    elif option == 2:
        e = int(input("Insira o valor de e: "))
        p = int(input("Insira o valor de p: "))
        q = int(input("Insira o valor de q: "))
        F = calculate_F_p_q(p, q)

    try:
        d = find_d(e, F)
        print(f"Para e = {e} e F = {F}, d = {d}")
    except ValueError as e:
        print(e)

def menu_calculate_F():
    p = int(input("Insira o valor de p: "))
    q = int(input("Insira o valor de q: "))
    F = calculate_F_p_q(p, q)
    print(f"Para p = {p} e q = {q}, F = {F}")

def menu_calculate_coprime():
    F = int(input("Insira o valor de F: "))
    e = find_coprime(F)
    if e is not None:
        print(f"Para F = {F}, e = {e}")
    else:
        print(f"Não há um coprimo para F = {F}.")

def main():
    menu = int(input("\nEscolha um número do menu:\n\n1 - Calcular d\n2 - Calcular F\n3 - Calcular e\n"))

    if menu == 1:
        menu_calculate_d()
    elif menu == 2:
        menu_calculate_F()
    elif menu == 3:
        menu_calculate_coprime()

if __name__ == "__main__":
    main()
