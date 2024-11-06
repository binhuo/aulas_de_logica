#Quartos do Hotel
matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

while True:
    andar = int(input("Qual andar fica o quarto?"))
    quarto = int(input("Qual o número do quarto?"))

    reserva = matriz[quarto-1][andar-1]

    if reserva != 0:
        print("O quarto já estava reservado!")
    else:
        print("Quarto disponível")
        print("Farei uma reserva:")
        matriz[quarto-1][andar-1] = 1
        print("O quarto foi reservado agora!")