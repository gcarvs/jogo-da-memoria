import random
tabuleiroDefault = [
    [' ', '|', '0', '1', '2', '3', '4', '5', '6', '7'],
    ['-', '/', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['0', '|'],
    ['1', '|'],
    ['2', '|'],
    ['3', '|'],
    ['4', '|']
]

tabuleiro = []

duplas8 = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H']
duplas12 = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H', 'I', 'I', 'J', 'J', 'L', 'L', 'M', 'M']
duplas20 = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H', 'I', 'I', 'J', 'J', 'L', 'L', 'M', 'M',
'N', 'N', 'O', 'O', 'P', 'P', 'Q', 'Q', 'R', 'R', 'S', 'S', 'T', 'T', 'U', 'U']

def gerarTabuleiro8():
    random.shuffle(duplas8)
    tabuleiro[0] = tabuleiroDefault[0][0:5]
    tabuleiro[1] = tabuleiroDefault[1][0:5]
    tabuleiro[2] = tabuleiroDefault[2]
    tabuleiro[3] = tabuleiroDefault[3]
    tabuleiro[4] = tabuleiroDefault[4]
    tabuleiro[5] = tabuleiroDefault[5]

    linhas = [duplas8[0:3], duplas8[4:7], duplas8[8:11], duplas8[12:15]]

    for idx, linha in linhas:
        count = 2
        for peca in linha:
            tabuleiro[idx + 2][count] = peca
            count++

def gerarTabuleiro12():
    random.shuffle(duplas12)
    tabuleiro[0] = tabuleiroDefault[0][0:7]
    tabuleiro[1] = tabuleiroDefault[1][0:7]
    tabuleiro[2] = tabuleiroDefault[2]
    tabuleiro[3] = tabuleiroDefault[3]
    tabuleiro[4] = tabuleiroDefault[4]
    tabuleiro[5] = tabuleiroDefault[5]

    linhas = [duplas12[0:5], duplas12[6:11], duplas12[12:17], duplas12[18:23]]

    for idx, linha in linhas:
        count = 2
        for peca in linha:
            tabuleiro[idx + 2][count] = peca
            count++

def gerarTabuleiro20():
    random.shuffle(duplas20)
    tabuleiro = tabuleiroDefault
    linhas = [duplas20[0:7], duplas20[8:15], duplas20[16:23], duplas20[24:31], duplas20[32, 39]]

    for idx, linha in linhas:
        count = 2
        for peca in linha:
            tabuleiro[idx + 2][count] = peca
            count++
        


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

    

