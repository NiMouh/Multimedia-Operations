

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


def zeros_compressao(string):
    codigoZeros = ""
    bits = 0
    i = 0
    while i < len(string):

        conta = 0
        while i < len(string) - 1 and (string[i] == "0" or string[i] == " "):
            conta += 1
            i += 1

        if conta >= 2:
            codigoZeros += "!" + str(conta)
            bits += 1
        else:
            i += 1
            codigoZeros += string[i - 1]
    print("O rácio de compressão é de: " + str(len(string) / (len(codigoZeros) - bits)))
    return codigoZeros


def menu():
    print("\n                # Bem-vindo à compressão #")
    print("===========================================================")
    print("1 -> Compressão em LZW.")
    print("2 -> Técnica RLE (Run-Length Encoding).")
    print("3 -> Técnicas de supressão de zeros ou espaços.")
    print("0 -> Terminar.\n")
    escolha = int(input("Escolha uma opção: "))
    return escolha


if __name__ == "__main__":
    opcao = menu()

    # Para a compressao de lzw
    ficheiro_leitura_lzw = open("Compressao/lzw.txt", "r")
    ficheiro_escrita_lzw = open("Compressao/enlzw.txt", "w")

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
            print("O código comprimido é: " + out_lzw)
        elif opcao == 2:
            out_tssr = rl_compressao(strrr)
            ficheiro_escrita_tssr.write(out_tssr)
            print("O código comprimido é: " + out_tssr)
        elif opcao == 3:
            out_zeros = zeros_compressao(strrr)
            ficheiro_escrita_tssr.write(out_zeros)
            print("O código comprimido é: " + out_zeros)
        else:
            print("Opção inválida.")
        opcao = menu()
    print("Encerrando...")

    # Fechando os ficheiros de leitura
    ficheiro_leitura_lzw.close()
    ficheiro_leitura_tssr.close()

    # Fechando os ficheiros de escrita
    ficheiro_escrita_lzw.close()
    ficheiro_escrita_tssr.close()
