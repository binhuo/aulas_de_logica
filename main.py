import random

def bingo():
    contagem = 0
    acertos = 0
    valores_chamados = set()

    # Gera valores aleatórios entre 1 e 25 (ajuste conforme necessário)
    while acertos < 25:
        valor = random.randint(1, 25)
        if valor not in valores_chamados:
            valores_chamados.add(valor)
            print(f"Valor chamado: {valor}")
            for linha in matriz:
                if valor in linha:
                    acertos += 1
                    break
        if acertos >= 25:
            print("BINGO!!!!")
            break
                
    return acertos

# Exemplo de uso:
matriz = [
    [5, 12, 7, 20, 12],
    [15, 8, 22, 10, 34],
    [9, 11, 6, 14, 23],
    [13, 25, 3, 9, 14]
]

# Inicia o processo de bingo
bingo()
