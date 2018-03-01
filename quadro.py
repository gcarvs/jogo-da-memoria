tabuleiro = [
    [' ', '|', '0', '1', '2', '3', '4', '5'],
    ['-', '/', '-', '-', '-', '-', '-', '-'],
    ['0', '|', 'A', 'B', 'C', 'D', 'E', 'F'],
    ['1', '|', 'A', 'B', 'C', 'D', 'E', 'F'],
    ['2', '|', 'G', 'H', 'I', 'J', 'L', 'M'],
    ['3', '|', 'G', 'H', 'I', 'J', 'L', 'M']
]

def fazerJogada():
    input1 = input('Digite as coordenadas da primeira peca(x,y): ')
    coordenadas1 = montarCoordenadas(input1)
    if coordenadas1:
        peca1 = tabuleiro[coordenadas1[0], coordenadas1[1]]
    else:
        print 'Coordenada invalida!'

    input2 = input('Digite as coordenadas da segunda peca(x,y): ')
    coordenadas2 = montarCoordenadas(input2)
    if coordenadas2:
        peca2 = tabuleiro[coordenadas2[0], coordenadas2[1]]
    else:
        print 'Coordenada invalida!'

    if peca1 == peca2:
        tabuleiro[coordenadas1[0], coordenadas1[1]] = '#'
        tabuleiro[coordenadas2[0], coordenadas2[1]] = '#'
        print 'Acertou!'
    else:
        print 'Errou!'

def montarCoordenadas(inputTxt):
    if(',' in inputTxt):
        if(len(inputTxt) == 3 and inputTxt[1] == ','):
            coordenadasTxt = inputTxt.split(',')
            if coordenadasTxt[0].isdigit() and coordenadasTxt[1].isdigit:
                x = int(coordenadasTxt[0]) + 2
                y = int(coordenadasTxt[1]) + 2
                if tabuleiro[x,y] == '#':
                    return False
                return [x, y]
            else:
                return False
    else
        return False

    

