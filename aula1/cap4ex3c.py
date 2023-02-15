n1 = float(input("Valor da Nota 1: "))
n2 = float(input("Valor da Nota 2: "))
n3 = float(input("Valor da Nota 3: "))
n4 = float(input("Valor da Nota 4: "))
nt=(n1+n2+n3+n4)/4
if nt>=5:
    print("a nota to aluno é " + str(nt) + " e ele passou")
else:
    print("a nota to aluno é " + str(nt) + " e ele não passou")
