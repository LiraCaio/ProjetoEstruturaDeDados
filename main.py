from PilhaEncadeada import Pilha
from Jogador import Jogador
from Baralho import Baralho


baralho = Baralho()
montante = list()

#Placar da partida
pontosDoJogador1 = 0
pontosDoJogador2 = 0
contadorDeJogadas = 0

print("---------- Batalha ---------- \n")

#Loop principal
while (True):
    

    
    print("Digite o nome do jogador 1")
    nomeDoJogador1 = input()
    jogador1 = Jogador(nomeDoJogador1)
    print()

    print("Digite o nome do jogador 2")
    nomeDoJogador2 = input()
    jogador2 = Jogador(nomeDoJogador2)
    print()

    n = 0
    while(n <= 25):
        n += 1
        jogador1.cartasDoJogador.empilha(baralho.retirarCarta())
        jogador2.cartasDoJogador.empilha(baralho.retirarCarta())

    while(contadorDeJogadas < 25):
        print(f"Jogada #{contadorDeJogadas}: \n")

        print(f"Carta do jogador(a) {jogador1.nome}: ")
        print(jogador1.cartasDoJogador.desempilha())
        print()
        
        print(f"Carta do jogador(a) {jogador2.nome}: ")
        print(jogador2.cartasDoJogador.desempilha())
        print()

        contadorDeJogadas += 1
    










