import random
palavra1 = ["maça","pão","carro","peixe","caminho","bolo","avião","navio","casa","predio","rua","helicoptero","cachorro","gato","cobra","arroz","chocolate","doce","avião","caminhão","papagaio","banheiro","quarto","cozinha","tubarão"]
vida = 5
aleatorio = 0
teste = 0
novo = 0
novo1 = len(palavra1[aleatorio])
jogo = True

while jogo:
    teste = palavra1[aleatorio]
    print(" Vida do jogador:",vida)
    print(end=teste[0:novo])
    print(end="_" * novo1)
    texto = input(" Adivinhe a Palavra, somente uma palavra: ")
    if texto in f"{palavra1[aleatorio]}":
        print()
        novo += 1
        novo1 -= 1

    if texto == f"{palavra1[aleatorio]}":
        print("Voce acertou!")
        novo = 0
        aleatorio = int(random.uniform(0,14))
        novo1 = len(palavra1[aleatorio])
    else:
        print("Quase!")
        vida -= 1
    if vida == 0:
        jogo = False
        print("\033[31mFim de jogo")
        print("Para jogar novamente reinicie o projeto")





