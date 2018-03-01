import random
import os
import time

tabuleiroDefault = [
    [' ', '|', '0', '1', '2', '3', '4', '5', '6', '7'],
    ['-', '/', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['0', '|', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['1', '|', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['2', '|', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['3', '|', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['4', '|', '#', '#', '#', '#', '#', '#', '#', '#']
]

tabuleiro = []

duplas8 = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H']
duplas12 = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H', 'I', 'I', 'J', 'J', 'L', 'L', 'M', 'M']
duplas20 = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H', 'I', 'I', 'J', 'J', 'L', 'L', 'M', 'M',
'N', 'N', 'O', 'O', 'P', 'P', 'Q', 'Q', 'R', 'R', 'S', 'S', 'T', 'T', 'U', 'U']

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def acabouJogo():
    achouPeca = False

    linhasValidas = tabuleiro[2:len(tabuleiro)]
    tabuleiroValido = [None] * len(tabuleiro)

    for idx, linha in enumerate(linhasValidas):
        tabuleiroValido[idx] = linha[2:len(linha)]

    for linha in tabuleiroValido:
        for peca in linha: 
            if peca != '#':
                return False
    
    return True
    

def gerarTabuleiro8():
    random.shuffle(duplas8)
    tabuleiro.append(tabuleiroDefault[0][0:6])
    tabuleiro.append(tabuleiroDefault[1][0:6])
    tabuleiro.append(tabuleiroDefault[2][0:6])
    tabuleiro.append(tabuleiroDefault[3][0:6])
    tabuleiro.append(tabuleiroDefault[4][0:6])
    tabuleiro.append(tabuleiroDefault[5][0:6])

    linhas = [duplas8[0:4], duplas8[4:8], duplas8[8:12], duplas8[12:16]]

    for idx, linha in enumerate(linhas):
        count = 2
        for peca in linha:
            tabuleiro[idx + 2][count] = peca
            count = count + 1

def gerarTabuleiro12():
    random.shuffle(duplas12)
    tabuleiro.append(tabuleiroDefault[0][0:8])
    tabuleiro.append(tabuleiroDefault[1][0:8])
    tabuleiro.append(tabuleiroDefault[2][0:8])
    tabuleiro.append(tabuleiroDefault[3][0:8])
    tabuleiro.append(tabuleiroDefault[4][0:8])
    tabuleiro.append(tabuleiroDefault[5][0:8])

    linhas = [duplas12[0:6], duplas12[6:12], duplas12[12:18], duplas12[18:24]]

    for idx, linha in enumerate(linhas):
        count = 2
        for peca in linha:
            tabuleiro[idx + 2][count] = peca
            count = count + 1

def gerarTabuleiro20():
    random.shuffle(duplas20)
    tabuleiro.append(tabuleiroDefault[0][0:10])
    tabuleiro.append(tabuleiroDefault[1][0:10])
    tabuleiro.append(tabuleiroDefault[2][0:10])
    tabuleiro.append(tabuleiroDefault[3][0:10])
    tabuleiro.append(tabuleiroDefault[4][0:10])
    tabuleiro.append(tabuleiroDefault[5][0:10])
    tabuleiro.append(tabuleiroDefault[6][0:10])
 
    linhas = [duplas20[0:8], duplas20[8:16], duplas20[16:24], duplas20[24:32], duplas20[32:40]]

    for idx, linha in enumerate(linhas):
        count = 2
        for peca in linha:
            tabuleiro[idx + 2][count] = peca
            count = count + 1

def printarTabuleiro():
    print 'Tabuleiro atual: \n'
    for linha in tabuleiro:
        linhaTxt = ''
        for peca in linha:
            if linhaTxt == '':
                if peca == '#':
                    linhaTxt += ' '
                elif peca.isdigit() or peca == '-' or peca == '|' or peca == '/' or peca == ' ':
                    linhaTxt += peca
                else: 
                    linhaTxt += '@'
            else:
                if peca == '#':
                    linhaTxt += '  '
                elif peca.isdigit() or peca == '-' or peca == '|' or peca == '/' or peca == ' ':
                    linhaTxt += ' ' + peca
                else:
                    linhaTxt += ' @'
                    
        print linhaTxt

def printarTabuleiroRevelado(coordenadas1, coordenadas2):
    print 'Tabuleiro atual: \n'
    for idxLinha, linha in enumerate(tabuleiro):
        linhaTxt = ''
        for idxPeca, peca in enumerate(linha):
            if linhaTxt == '':
                if peca == '#':
                    linhaTxt += ' '
                elif peca.isdigit() or peca == '-' or peca == '|' or peca == '/' or peca == ' ' or (idxLinha == coordenadas1[0] and idxPeca == coordenadas1[1]) or (idxLinha == coordenadas2[0] and idxPeca == coordenadas2[1]):
                    linhaTxt += peca
                else: 
                    linhaTxt += '@'
            else:
                if peca == '#':
                    linhaTxt += ' '
                elif peca.isdigit() or peca == '-' or peca == '|' or peca == '/' or peca == ' 'or (idxLinha == coordenadas1[0] and idxPeca == coordenadas1[1]) or (idxLinha == coordenadas2[0] and idxPeca == coordenadas2[1]):
                    linhaTxt += ' ' + peca
                else:
                    linhaTxt += ' @'
                    
        print linhaTxt


def fazerJogada():
    input1 = input('Digite as coordenadas da primeira peca(x,y): ')
    coordenadas1 = montarCoordenadas(input1)
    while not coordenadas1:
        print 'Coordenada invalida!'
        input1 = input('Digite as coordenadas da primeira peca(x,y): ')
        coordenadas1 = montarCoordenadas(input1)

    peca1 = tabuleiro[coordenadas1[0]][coordenadas1[1]]
        

    input2 = input('Digite as coordenadas da segunda peca(x,y): ')
    coordenadas2 = montarCoordenadas(input2)

    while not coordenadas2:
        print 'Coordenada invalida!'
        input2 = input('Digite as coordenadas da segunda peca(x,y): ')
        coordenadas2 = montarCoordenadas(input2)

    peca2 = tabuleiro[coordenadas2[0]][coordenadas2[1]]    
    
    cls()
    printarTabuleiroRevelado(coordenadas1, coordenadas2)
    if peca1 == peca2:
        tabuleiro[coordenadas1[0]][coordenadas1[1]] = '#'
        tabuleiro[coordenadas2[0]][coordenadas2[1]] = '#'
        print 'Acertou!'
    else:
        print 'Errou!'

    time.sleep(5)

def montarCoordenadas(inputTxt):
    if(',' in inputTxt):
        if(len(inputTxt) == 3 and inputTxt[1] == ','):
            coordenadasTxt = inputTxt.split(',')
            if coordenadasTxt[0].isdigit() and coordenadasTxt[1].isdigit():
                x = int(coordenadasTxt[0]) + 2
                y = int(coordenadasTxt[1]) + 2
                if x >= len(tabuleiro):
                    return False
                elif y >= len(tabuleiro[x]):
                    return False
                elif tabuleiro[x][y] == '#':
                    return False
                return [x, y]
            else:
                return False
    else:
        return False

def jogar():
    print 'Bem vindo ao jogo da memoria!!'
    print 'Em qual dificuldade deseja jogar?'
    print 'a) Facil (8 duplas)'
    print 'b) Medio (12 duplas)'
    print 'c) Dificil (20 duplas)'
    
    dificuldade = input('Entre com opcao: ')
    while dificuldade != 'a' and dificuldade != 'b' and dificuldade != 'c':
        print 'Opcao invalida! Entre apenas com a letra a, b ou c.'
        dificuldade = input('Entre com opcao: ')
    
    if dificuldade == 'a':
        gerarTabuleiro8()
    elif dificuldade == 'b':
        gerarTabuleiro12()
    else:
        gerarTabuleiro20()
    
    cls()
    printarTabuleiro()

    while not acabouJogo():
        fazerJogada()
        cls()
        printarTabuleiro()
    
    cls()

    print 'Obrigado por jogar nosso jogo da memoria!!'

jogar()