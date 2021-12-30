import cv2

video = cv2.VideoCapture('Video/video.mp4')

largura_quadro = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
altura_quadro = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

tamanho = (largura_quadro, altura_quadro)

fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V')

novo_video = cv2.VideoWriter('Video/blacknwhite_video.mp4', fourcc, 30.0, tamanho)

while True:

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

video.release()
novo_video.release()
cv2.destroyAllWindows()
