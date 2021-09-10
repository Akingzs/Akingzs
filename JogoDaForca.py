
palavra = input('Entre com a palavra a ser descoberta: ')
# print("\n" * 130)
letraslista = []
chances = 2
while True:

    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print(f'{letra} não é uma letra, digite novamente')
        continue

    letraslista.append(letra)

    if letra in palavra:
        print(f'A letra {letra} existe na palavra')
    else:
        print(f'Que pena! Não existe a letra {letra} na palavra')
        letraslista.pop()

    ver_palavra = ''
    for letra_oculta in palavra:
        if letra_oculta in letraslista:
            ver_palavra += letra_oculta
        else:
            ver_palavra += '*'

    if ver_palavra == palavra:
        print(f'Parabens!! você ganhou, a palavra era: {ver_palavra}.')
        break
    else:
        print(f'A palavra secreta está assim: {ver_palavra}')

    if letra not in letraslista:
        chances -= 1
        print(f'Voce ainda tem {chances} chances')
    if chances < 0:
        break


