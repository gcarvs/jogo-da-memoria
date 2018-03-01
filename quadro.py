import socket
import pickle
import random
import os
import time

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect(('localhost', 12397))

def abrirConexao():
    try:
        # Tenta se conectar ao servidor
        s.connect(('localhost', 12397))
        msg = "Ola servidor!\n"
        # Envia mensagem codificada em bytes ao servidor
        s.send(msg.encode('ascii'))        
    except Exception as erro:
        print(str(erro))

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def fazerJogada():
    input1 = input('Digite as coordenadas da primeira peca(x,y): ')
    s.send(input1.encode('ascii'))
    encodedValid = s.recv(1024)
    isValid = pickle.loads(encodedValid)

    while not isValid:
        print('Coordenada invalida!')
        input1 = input('Digite as coordenadas da primeira peca(x,y): ')
        s.send(input1.encode('ascii'))
        encodedValid = s.recv(1024)
        isValid = pickle.loads(encodedValid) 

    coordenadasTxt = input1.split(',')
    x = int(coordenadasTxt[0]) + 2
    y = int(coordenadasTxt[1]) + 2  

    input2 = input('Digite as coordenadas da segunda peca(x,y): ')
    s.send(input2.encode('ascii'))
    encodedValid = s.recv(1024)
    isValid = pickle.loads(encodedValid)

    while not isValid:
        print('Coordenada invalida!')
        input2 = input('Digite as coordenadas da segunda peca(x,y): ')
        s.send(input2.encode('ascii'))
        encodedValid = s.recv(1024)
        isValid = pickle.loads(encodedValid)  

    coordenadasTxt2 = input2.split(',')
    x2 = int(coordenadasTxt2[0]) + 2
    y2 = int(coordenadasTxt2[1]) + 2     
    
    jogadas = [[x, y], [x2, y2]]

    s.send(pickle.dumps(jogadas))
    cls()
    txt = s.recv(1024)
    print(txt.decode('ascii'))
   

def jogar():
    print('Bem vindo ao jogo da memoria!!')
    print('Em qual dificuldade deseja jogar?')
    print('a) Facil (8 duplas)')
    print('b) Medio (12 duplas)')
    print('c) Dificil (20 duplas)')
    
    dificuldade = input('Entre com opcao: ')
    while dificuldade != 'a' and dificuldade != 'b' and dificuldade != 'c':
        print('Opcao invalida! Entre apenas com a letra a, b ou c.')
        dificuldade = input('Entre com opcao: ')

    s.send(dificuldade.encode('ascii'))
    
    cls()

    tabuleiro = s.recv(1024).decode('ascii')
    while tabuleiro != 'O jogo acabou':
        print(tabuleiro)
        fazerJogada()
        time.sleep(5)
        cls()
        tabuleiro = s.recv(1024).decode('ascii')
    
    cls()

    print('Obrigado por jogar nosso jogo da memoria!!')

jogar()