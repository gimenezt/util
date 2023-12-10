def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    else:
        m, n, o = extended_euclidean(b % a, a)
        return m, o - (b // a) * n, n

def find_d(e, F):
    m, x, y = extended_euclidean(e, F)
    if m != 1:
        raise ValueError(f"{e} is not invertible modulo {F}")
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
    option = int(input("You have:\n1 - The values of p and q\n2 - The value of F\n3 - The value of n"))

    if option == 1:
        e = int(input("Enter the value of e: "))
        F = int(input("Enter the value of F: "))

    elif option == 2:
        e = int(input("Enter the value of e: "))
        p = int(input("Enter the value of p: "))
        q = int(input("Enter the value of q: "))
        F = calculate_F_p_q(p, q)

    elif option == 3:
        n = int(input("Enter the value of n: "))
        e = int(input("Enter the value of e: "))

    try:
        d = find_d(e, F)
        print(f"For e = {e} and F = {F}, d = {d}")
    except ValueError as e:
        print(e)

def menu_calculate_F():
    p = int(input("Enter the value of p: "))
    q = int(input("Enter the value of q: "))
    F = calculate_F_p_q(p, q)
    print(f"For p = {p} and q = {q}, F = {F}")

def menu_calculate_coprime():
    F = int(input("Enter the value of F: "))
    e = find_coprime(F)
    if e is not None:
        print(f"For F = {F}, e = {e}")
    else:
        print("Could not find a coprime for F.")

def main():
    menu = int(input("1 - Calculate the value of d\n2 - Calculate the value of F\n3 - Calculate the value of e\n"))

    if menu == 1:
        menu_calculate_d()
    elif menu == 2:
        menu_calculate_F()
    elif menu == 3:
        menu_calculate_coprime()

if __name__ == "__main__":
    main()