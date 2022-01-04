from pydub import AudioSegment


def corta_audio(primeiro_tempo, segundo_tempo, audio):

    # Conversão dos tempos dados para segundos
    t1 = primeiro_tempo * 1000
    t2 = segundo_tempo * 1000

    # Declaração do "audio_cortado" como sendo igual uma fração do vetor do audio original e exportação do mesmo
    audio_cortado = audio[t1:t2]
    audio_cortado.export('Som/corte.wav', format="wav")


def junta_audio(primeiro_audio, segundo_audio):

    # Declaração do "juncao_audio" como sendo igual ao produto dos vetores dos audios originais e exportação do mesmo
    juncao_audio = primeiro_audio * segundo_audio
    juncao_audio.export('Som/juncao.wav', format="wav")


def normaliza_audio(valor_dbfs, audio):
    amplitude = valor_dbfs - audio.dBFS

    # Declaração do "audio_normalizado" sendo igual ao audio original + o valor da amplitude e exportação do mesmo
    audio_normalizado = audio + amplitude
    audio_normalizado.export("Som/normalizado.wav", format="wav")


def abranda_audio(velocidade, audio):

    audio_slowed = audio
    slowed = 1 - velocidade

    audio_slowed.frame_rate *= slowed
    audio_slowed.export("Som/slowed.wav", format="wav")


def atraso_audio(atraso_ms, audio):

    audio_delay = AudioSegment.empty()
    for x in range(atraso_ms):
        audio_delay.split_to_mono().append(0)
    audio_delay.split_to_mono().append(audio)
    audio_delay.export("Som/delay.wav", format="wav")


def menu():
    print("\n<--- Bem-vindo à edição de audio --->\n")
    print("1: Cortar parte de um audio.")
    print("2: Juntar 2 audios.")
    print("3: Normalizar um audio.")
    print("4: Abrandar um audio.")
    print("5: Colocar atraso (delay) num audio.")
    print("0: Terminar.\n")
    escolha = int(input("Escolha uma opção: "))
    return escolha


if __name__ == "__main__":
    opcao = menu()

    # Inicializa os audios
    audio_um = AudioSegment.from_wav('Som/som1.wav')
    audio_dois = AudioSegment.from_wav('Som/som2.wav')
    audio_tres = AudioSegment.from_wav('Som/som3.wav')

    while opcao != 0:
        if opcao == 1:
            tempo1 = int(input("Qual o primeiro tempo do corte (em segundos): "))
            tempo2 = int(input("Qual o segundo tempo do corte (em segundos): "))
            corta_audio(tempo1, tempo2, audio_um)
            print("Opção 1 foi concluída.")
        elif opcao == 2:
            junta_audio(audio_um, audio_dois)
            print("Opção 2 foi concluída.")
        elif opcao == 3:
            valor = float(input("Qual o valor da normalização que pretende (em dBS): "))
            normaliza_audio(valor, audio_tres)
            print("Opção 3 foi concluída.")
        elif opcao == 4:
            vel = float(input("Que a percentagem de abrandamento pretende que o video tenha (decimal): "))
            abranda_audio(vel, audio_um)
            print("Opção 4 foi concluída.")
        elif opcao == 5:
            delay = int(input("Qual o delay que pretende (em ms): "))
            atraso_audio(delay, audio_dois)
            print("Opção 5 foi concluída.")
        else:
            print("Opção inválida.")

        # Volta a printar o menu
        opcao = menu()
