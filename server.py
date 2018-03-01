import socket
import pickle
import random
import time

# Cria o socket
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente = ''
# Obtém o nome da máquina
# host = socket.gethostname()
host = "localhost"
porta = 12397
# Associa a porta
socket_servidor.bind((host, porta))
# Escutando...
socket_servidor.listen()
print("Servidor de nome ", host, " esperando conexão na porta ", porta)

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

duplas8 = ['A', 'A', 'B', 'B', 'C', 'C', 'D',
    'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H']
duplas12 = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F',
    'F', 'G', 'G', 'H', 'H', 'I', 'I', 'J', 'J', 'L', 'L', 'M', 'M']
duplas20 = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H', 'I', 'I', 'J', 'J', 'L', 'L', 'M', 'M',
'N', 'N', 'O', 'O', 'P', 'P', 'Q', 'Q', 'R', 'R', 'S', 'S', 'T', 'T', 'U', 'U']


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

    linhas = [duplas20[0:8], duplas20[8:16],
        duplas20[16:24], duplas20[24:32], duplas20[32:40]]

    for idx, linha in enumerate(linhas):
        count = 2
        for peca in linha:
            tabuleiro[idx + 2][count] = peca
            count = count + 1


def printarTabuleiro():
    txt = 'Tabuleiro atual: \n'
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
        txt += linhaTxt + '\n'
    return txt


def printarTabuleiroRevelado(coordenadas1, coordenadas2):
    txt = 'Tabuleiro atual: \n'
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
        txt += linhaTxt + '\n'
    return txt


def fazerJogada():
    print('fazerjogada')
    input1 = socket_cliente.recv(1024)
    isValid = validarJogada(input1.decode('ascii'))
    socket_cliente.send(pickle.dumps(isValid))

    input2 = socket_cliente.recv(1024)
    isValid = validarJogada(input2.decode('ascii'))
    socket_cliente.send(pickle.dumps(isValid))

    jogadas = pickle.loads(socket_cliente.recv(1024))

    peca1 = tabuleiro[jogadas[0][0]][jogadas[0][1]]
    peca2 = tabuleiro[jogadas[1][0]][jogadas[1][1]]

    txt = printarTabuleiroRevelado(jogadas[0], jogadas[1])
    if peca1 == peca2:
        tabuleiro[jogadas[0][0]][jogadas[0][1]] = '#'
        tabuleiro[jogadas[1][0]][jogadas[1][1]] = '#'
        txt += 'Acertou!'
    else:
        txt += 'Errou!\n'
    socket_cliente.send(txt.encode('ascii'))


def validarJogada(inputTxt):
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
                return True
            else:
                return False
    else:
        return False


def setDificuldade(dificuldade):
    if dificuldade == 'a':
        gerarTabuleiro8()
    elif dificuldade == 'b':
        gerarTabuleiro12()
    else:
        gerarTabuleiro20()


while True:
    (socket_cliente, addr) = socket_servidor.accept()
    print('Conectado a:' + str(addr))
    dificuldade = socket_cliente.recv(1024)
    setDificuldade(dificuldade.decode('ascii'))
    while not acabouJogo():
        time.sleep(2)
        socket_cliente.send(printarTabuleiro().encode('ascii'))
        fazerJogada()
    socket_cliente.send('O jogo acabou'.encode('ascii'))
    socket_cliente.close()
