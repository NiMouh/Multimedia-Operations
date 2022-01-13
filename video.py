import cv2


def pretoebrancovid(vid):
    # Determina a resolução do video capturado
    largura_quadro = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    altura_quadro = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    tamanho = (largura_quadro, altura_quadro)

    # Define o formato do video
    fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V')
    fps = vid.get(cv2.CAP_PROP_FPS)

    # Inicializa o novo video
    novo_video = cv2.VideoWriter('Video/blacknwhite_video.mp4', fourcc, fps, tamanho)

    while True:

        # Leitura dos frames
        existeQuadro, quadro = video.read()

        if existeQuadro:
            for x in range(0, largura_quadro - 1):
                for y in range(0, altura_quadro - 1):
                    r, g, b = quadro[y, x]
                    cinza = r * 0.2125 + g * 0.7174 + b * 0.0721
                    quadro[y, x] = [cinza, cinza, cinza]
            novo_video.write(quadro)
        else:
            break
    novo_video.release()


def negativovid(vid):
    # Determina a resolução do video capturado
    largura_quadro = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    altura_quadro = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    tamanho = (largura_quadro, altura_quadro)

    # Define o formato do video
    fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V')
    fps = vid.get(cv2.CAP_PROP_FPS)

    # Inicializa o novo video
    novo_video = cv2.VideoWriter('Video/negativo_video.mp4', fourcc, fps, tamanho)

    while True:

        # Leitura dos frames
        existeQuadro, quadro = video.read()

        if existeQuadro:
            for x in range(0, largura_quadro - 1):
                for y in range(0, altura_quadro - 1):
                    r, g, b = quadro[y, x]
                    quadro[y, x] = [255 - r, 255 - g, 255 - b]
            novo_video.write(quadro)
        else:
            break
    novo_video.release()


def invertidovid(vid):
    # Determina a resolução do video capturado
    largura_quadro = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    altura_quadro = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    tamanho = (largura_quadro, altura_quadro)

    # Define o formato do video
    fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V')
    fps = vid.get(cv2.CAP_PROP_FPS)

    # Inicializa o novo video
    novo_video = cv2.VideoWriter('Video/invertido_video.mp4', fourcc, fps, tamanho)

    while True:

        # Leitura dos frames
        existeQuadro, quadro = video.read()

        if existeQuadro:

            # Considerar o novo quadro como uma cópia do original
            novoquadro = quadro.copy()

            for x in range(0, largura_quadro - 1):
                for y in range(0, altura_quadro - 1):
                    novoquadro[y, (largura_quadro - x) - 1] = quadro[y, x]
            novo_video.write(novoquadro)
        else:
            break
    novo_video.release()


def menu():
    print("\n<--- Bem-vindo à edição de videos --->\n")
    print("1: Transformar um video no seu preto e branco.")
    print("2: Transformar um video no seu negativo.")
    print("3: Transformar um video no seu inverso.")
    print("0: Terminar.\n")
    escolha = int(input("Escolha uma opção: "))
    return escolha


if __name__ == "__main__":
    opcao = menu()

    while opcao != 0:

        # Inicializa o video
        video = cv2.VideoCapture('Video/video.mp4')

        if opcao == 1:
            pretoebrancovid(video)
            print("Operação 1 foi concluída.")
        elif opcao == 2:
            negativovid(video)
            print("Operação 2 foi concluída.")
        elif opcao == 3:
            invertidovid(video)
            print("Operação 3 foi concluída.")
        else:
            print("Opção inválida.")

        # Volta a printar o menu
        opcao = menu()
