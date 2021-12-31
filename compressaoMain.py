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
    print("O rácio de compressão é de: " + str(len(string) / len(codigoP)))
    return codigoP


def rl_compressao(string):
    codigoRL = ""
    i = 0
    while i < len(string):

        conta = 1
        while i < len(string) - 1 and string[i] == string[i + 1]:
            conta += 1
            i += 1
        i += 1

        if conta >= 2:
            codigoRL += str(conta) + "!" + string[i - 1]
        else:
            codigoRL += string[i - 1]
    print("O rácio de compressão é de: " + str(len(string) / len(codigoRL)))
    return codigoRL


def menu():
    print("\n<--- Bem-vindo á compressão --->\n")
    print("1: Compressão em LZW.")
    print("2: Técnica Run-Length Encoding (RLE).")
    print("0: Terminar.\n")
    escolha = int(input("Escolha uma opção: "))
    return escolha


if __name__ == "__main__":
    opcao = menu()

    # Para a compressao de lzw
    ficheiro_leitura_lzw = open("Compressao/comp.txt", "r")
    ficheiro_escrita_lzw = open("Compressao/comp2.txt", "w")

    strr = ficheiro_leitura_lzw.read()
    strr = strr + '\0'

    # Para as Técnicas de supressão de sequências repetitivas
    ficheiro_leitura_tssr = open("Compressao/tssr.txt", "r")
    ficheiro_escrita_tssr = open("Compressao/entssr.txt", "w")

    strrr = ficheiro_leitura_tssr.read()

    while opcao != 0:
        if opcao == 1:
            out_lzw = lzw_compressao(strr)
            ficheiro_escrita_lzw.write(out_lzw)
            print(out_lzw)
        elif opcao == 2:
            out_tssr = rl_compressao(strrr)
            ficheiro_escrita_tssr.write(out_tssr)
            print(out_tssr)
        else:
            print("Opção inválida.")
        opcao = menu()

    # Fechando os ficheiros de leitura
    ficheiro_leitura_lzw.close()
    ficheiro_leitura_tssr.close()

    # Fechando os ficheiros de escrita
    ficheiro_escrita_lzw.close()
    ficheiro_escrita_tssr.close()
