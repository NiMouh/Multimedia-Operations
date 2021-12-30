from PIL import Image


def adicao(primeira_imagem, segunda_imagem):

    adicao_imagem = Image.new("RGB", primeira_imagem.size, 'White')

    for i in range(0, adicao_imagem.width):
        for j in range(0, adicao_imagem.height):

            pixel1 = primeira_imagem.getpixel((i, j))
            pixel2 = segunda_imagem.getpixel((i, j))

            R = pixel1[0] + pixel2[0]
            if R > 255:
                R = 255

            G = pixel1[1] + pixel2[1]
            if G > 255:
                G = 255

            B = pixel1[2] + pixel2[2]
            if B > 255:
                B = 255

            adicao_imagem.putpixel((i, j), (R, G, B))
    adicao_imagem.save("Imagens/adicao.jpg")


def subtracao(primeira_imagem, segunda_imagem):

    subtracao_imagem = Image.new("RGB", primeira_imagem.size, 'White')

    for i in range(0, subtracao_imagem.width):
        for j in range(0, subtracao_imagem.height):

            pixel1 = primeira_imagem.getpixel((i, j))
            pixel2 = segunda_imagem.getpixel((i, j))

            R = pixel1[0] - pixel2[0]
            if R < 0:
                R = 0

            G = pixel1[1] - pixel2[1]
            if G < 0:
                G = 0

            B = pixel1[2] - pixel2[2]
            if B < 0:
                B = 0

            subtracao_imagem.putpixel((i, j), (R, G, B))
    subtracao_imagem.save("Imagens/subtracao.jpg")


def and_imagem(primeira_imagem, segunda_imagem):

    and_img = Image.new("RGB", primeira_imagem.size, 'White')

    for i in range(0, and_img.width):
        for j in range(0, and_img.height):
            pixel1 = primeira_imagem.getpixel((i, j))
            pixel2 = segunda_imagem.getpixel((i, j))

            pixel3 = tuple(pixel1 & pixel2 for pixel1, pixel2 in zip(pixel1, pixel2))

            and_img.putpixel((i, j), pixel3)
    and_img.save("Imagens/and.jpg")


def or_imagem(primeira_imagem, segunda_imagem):

    or_img = Image.new("RGB", primeira_imagem.size, 'White')

    for i in range(0, or_img.width):
        for j in range(0, or_img.height):
            pixel1 = primeira_imagem.getpixel((i, j))
            pixel2 = segunda_imagem.getpixel((i, j))

            pixel3 = tuple(pixel1 | pixel2 for pixel1, pixel2 in zip(pixel1, pixel2))

            or_img.putpixel((i, j), pixel3)
    or_img.save("Imagens/or.jpg")


def preto_e_branco(imagem):

    preto_branco_img = Image.new("RGB", imagem.size, 'White')

    for i in range(0, preto_branco_img.width):
        for j in range(0, preto_branco_img.height):
            pixel1 = imagem.getpixel((i, j))

            R = pixel1[0]

            G = pixel1[1]

            B = pixel1[2]

            bw = int((R + B + G) / 3)

            preto_branco_img.putpixel((i, j), (bw, bw, bw))
    preto_branco_img.save("Imagens/pretoebranco.jpg")


def negativo(imagem):

    negativo_img = Image.new("RGB", imagem.size, 'White')

    for i in range(0, negativo_img.width):
        for j in range(0, negativo_img.height):
            pixel1 = imagem.getpixel((i, j))

            R = 255 - pixel1[0]

            G = 255 - pixel1[1]

            B = 255 - pixel1[2]

            negativo_img.putpixel((i, j), (R, G, B))
    negativo_img.save("Imagens/negativo.jpg")


def invertida(imagem):

    invertida_img = Image.new("RGB", imagem.size, 'White')

    for i in range(0, invertida_img.width):
        for j in range(0, invertida_img.height):
            pixel1 = imagem.getpixel((i, j))
            ip = (imagem.width - i) - 1

            invertida_img.putpixel((ip, j), pixel1)
    invertida_img.save("Imagens/invetida.jpg")


def menu():
    print("<--- Bem-vindo á edição de imagens --->\n")
    print("1: Fazer adição entre 2 imagens.")
    print("2: Fazer subtração entre 2 imagens.")
    print("3: Fazer AND lógico entre 2 imagens.")
    print("4: Fazer OR lógico entre 2 imagens.")
    print("5: Transformar uma imagem a cores numa em preto e branco.")
    print("6: Transformar uma imagem no seu negativo.")
    print("7 : Transformar uma imagem no seu inverso.")
    print("0: Terminar. \n")
    escolha = int(input("Escolha uma opção: "))
    return escolha


if __name__ == "__main__":
    opcao = menu()

    imagem_primaria = Image.open("Imagens/image1.jpg")
    imagem_secundaria = Image.open("Imagens/image2.jpg")
    imagem_terciaria = Image.open("Imagens/image3.jpg")

    while opcao != 0:
        if opcao == 1:
            adicao(imagem_primaria, imagem_secundaria)
            print("Opção 1 foi concluída.")
        elif opcao == 2:
            subtracao(imagem_primaria, imagem_secundaria)
            print("Opção 2 foi concluída.")
        elif opcao == 3:
            and_imagem(imagem_primaria, imagem_secundaria)
            print("Opção 3 foi concluída.")
        elif opcao == 4:
            or_imagem(imagem_primaria, imagem_secundaria)
            print("Opção 4 foi concluída.")
        elif opcao == 5:
            preto_e_branco(imagem_primaria)
            print("Opção 5 foi concluída.")
        elif opcao == 6:
            negativo(imagem_terciaria)
            print("Opção 6 foi concluída.")
        elif opcao == 7:
            invertida(imagem_primaria)
            print("Opção 7 foi concluída.")
        else:
            print("Opção inválida.")
        opcao = menu()
