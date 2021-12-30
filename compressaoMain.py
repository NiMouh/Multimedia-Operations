

def lzw_compressao(string):
    dicionario = []

    for letra in string:
        if not dicionario.__contains__(letra):
            dicionario.append(letra)
    dicionario = sorted(dicionario)
    dicionario.remove('\x00')

    codigoP = ""

    P = string[0]

    for i in range(1, len(string)):
        C = string[i]
        if dicionario.__contains__(P + C):
            P = P + C
        else:
            codigoP = codigoP + str(dicionario.index(P) + 1)
            dicionario.append(P + C)
            P = C
    return codigoP


""""
O algoritmo de codificação funciona da seguinte forma (RUN-LENGTH):

- Determinar uma FLAG que não exista no texto a comprimir.
- Ler um caracter. Ler os próximos caracteres enquanto forem iguais ao primeiro caracter lido.
- Se o número total de caracteres lidos for igual ou superior a 4, 
comprimir essa cadeia de caracteres da seguinte forma: FLAG + nº de repetições + caracter.
- Se o numero total de caracteres lidos for inferior a 4, não se efetua compressão, 
logo essa cadeia de caracteres permanece inalterável.
"""


def menu():
    print("<--- Bem-vindo á compressão --->\n")
    print("1: Compressão em LZW.")
    print("2: Técnicas de supressão de sequências repetitivas.")
    print("0: Terminar.\n")
    escolha = int(input("Escolha uma opção: "))
    return escolha


if __name__ == "__main__":
    opcao = menu()

    ficheiro_leitura = open("Compressao/comp.txt", "r")
    ficheiro_escrita = open("Compressao/comp2.txt", "w")

    strr = ficheiro_leitura.read()
    strr = strr + '\0'
    while opcao != 0:
        if opcao == 1:
            out = lzw_compressao(strr)
            ficheiro_escrita.write(out)
            print(out)

            print("O rácio de compressão é de:")
            print(len(strr)/len(out))
        elif opcao == 2:
            print("OPÇÃO 2")
        else:
            print("Opção inválida.")
        opcao = menu()
    ficheiro_leitura.close()
    ficheiro_escrita.close()
