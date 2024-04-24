print("\n======  CALCULADORA  ======")
print("\nOlá!\nEsse programa foi feito para calcular o CR de um quadrimestre\na partir de seus conceitos finais nas disciplinas.")

n = int(input("\nDigite o número de matérias cursadas nesse QUAD: "))

grade_weight = {"A":4, "B":3,"C":2,"D":1,"F":0,"O":0}

sum_grades = 0
total_cred = 0

for i in range(n):
    grade = input(f"Digite o conceito (A, B, C, D, F, O) da {i+1}º disciplina: ").capitalize()
    cred = int(input(f"Agora, digite o conceito a quantidade de créditos dessa disciplina: "))
    
    grade = grade_weight[grade]
    sum_grades = sum_grades + (grade*cred)
    print(sum_grades)
    total_cred = total_cred+cred

cr = sum_grades/total_cred
print("\n======  RESULTADO  ======")
print(f"\nCR final do quadrimestre: {cr}\n")


    
    



