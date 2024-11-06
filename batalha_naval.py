tabuleiro = [['~'] * 10 for i in range(10)] #Tabuleiro em uma matriz 10 X 10

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))
    print()

#imprimir_tabuleiro(tabuleiro)

def colocar_navio(tabuleiro, linha_inicial, coluna_inicial,tamanho,orientacao):
    if orientacao == 'horizontal':
        for i in range(tamanho):
            tabuleiro[linha_inicial][coluna_inicial * i] = '#'
    elif orientacao == 'vertical':
        for i in range(tamanho):
            tabuleiro[linha_inicial * i][coluna_inicial] = '#'
    

def dar_tiro(tabuleiro,linha, coluna):
    if tabuleiro[linha][coluna] == '#':
        tabuleiro[linha][coluna] = 'X'
        print("Que tiro foi esse?!")
        return True
    elif tabuleiro[linha][coluna] =="~":
        tabuleiro[linha][coluna] = "o"
        print("Eroooou!")   
        return False
    else:         
        print("Você já atirou aqui!")
        return False
    

#colocar_navio(tabuleiro,1,1,3,'vertical')
#imprimir_tabuleiro(tabuleiro)
#dar_tiro(tabuleiro,2,1)
#imprimir_tabuleiro(tabuleiro)

def jogo():
    #Cria dois tabuleiros dos jogadores
    tamanho = 10
    tabuleiro_jogador1 = [['~'] * tamanho for _ in range(tamanho)]
    tabuleiro_jogador2 = [['~'] * tamanho for _ in range(tamanho)]

    #colocar os navios nas posições
    colocar_navio(tabuleiro_jogador1,1,2,3,'vertical')
    colocar_navio(tabuleiro_jogador2,3,2,4,'horizontal')

    while True:
        print("Jogodor 1 atirando:")
        imprimir_tabuleiro(tabuleiro_jogador2)

        x = int(input("Jogador 1 escolha a linha de tiro (0,9): "))
        y = int(input("Jogador 1 escolha a coluna de tiro (0,9): "))
        dar_tiro(tabuleiro_jogador2,x,y)
    
        #Verificar
        if all(cell !='#' for row in tabuleiro_jogador2 for cell in row):
            print("Jogador 1 ganhou!")
            break
    
        print("Jogodor 2 atirando:")
        imprimir_tabuleiro(tabuleiro_jogador1)

        x = int(input("Jogador 2 escolha a linha de tiro (0,9): "))
        y = int(input("Jogador 2 escolha a coluna de tiro (0,9): "))
        dar_tiro(tabuleiro_jogador1,x,y)
    
        #Verificar
        if all(cell !='#' for row in tabuleiro_jogador1 for cell in row):
            print("Jogador 2 ganhou!")
            break   

jogo()            
             
        