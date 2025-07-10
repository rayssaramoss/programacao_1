def jogo_adivinhacao(num_secreto):
    palpite = 0

    while palpite != num_secreto:
        try:
            palpite_usuario = (input("Digite seu palpite: "))
            palpite = int(palpite_usuario)

            if palpite > num_secreto:
                print("Maior que o número secreto")
            elif palpite < num_secreto: 
                print("Menor que o número secreto")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    
    print("parabens, voce acertou")

jogo_adivinhacao(7)
