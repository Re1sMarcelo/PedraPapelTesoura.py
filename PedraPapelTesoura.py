# PedraPapelTesoura
#Programa de pedra papel tesoura contra a  maquina


from random import choice #do modulo random vou importar a funcao choice 

jogador_vitorias = 0
maquina_vitorias = 0

def opcao_jogador():
    esc_jogador = input("escolha pedra, papel ou tesoura: ")
    esc_jogador.lower()
    if esc_jogador == "pedra":
        return esc_jogador
    elif esc_jogador == "papel":
        return esc_jogador
    elif esc_jogador == "tesoura":
        return esc_jogador
    else:
        print("voce escolheu uma opcao invalida, tente novamente!")
        opcao_jogador()


def opcao_Maquina():
    esc_maquina = choice (["pedra", "papel", "tesoura"])
    return esc_maquina



while True:

    print("-" *30)
    esc_jogador = opcao_jogador()
    esc_maquina = opcao_Maquina() 
    print("-" *30)

    if (esc_jogador == "pedra") and (esc_maquina == "tesoura") \
        or (esc_jogador == "papel") and (esc_maquina == "pedra") \
            or (esc_jogador == "tesoura") and (esc_maquina == "papel"):
            #jogador ganha
            print (f"jogador escolheu {esc_jogador} e a maquina escolheu {esc_maquina} " \
            " resultado: Voce ganhou! ")
            jogador_vitorias += 1

    elif esc_jogador == esc_maquina: #empate
        print (f"jogador escolheu: {esc_jogador} e a maquina escolheu: {esc_maquina} " \
            " resultado: empate! ")
    else: #maquina ganha
        print (f"jogador escolheu: {esc_jogador} e a maquina escolheu: {esc_maquina} " \
            " resultado: Voce perdeu! ")
        maquina_vitorias += 1

    print("-" *30)
    print(f"vitorias do jogador: {jogador_vitorias}")
    print(f"vitorias da maquina: {maquina_vitorias}")
    print("-" *30)

    esc_jogador = input("voce quer jogar novamente? ")
    if esc_jogador in ["SIM", "sim", "Sim", "S", "s"]:
        pass
    elif esc_jogador in ["NAO", "nao", "Nao", "N", "n"]:
        break
    else:
        break

