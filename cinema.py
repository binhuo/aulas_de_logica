def reservar(sala, fileira, assento):
    if sala[fileira-1][assento-1] == 0:
        sala[fileira-1][assento-1] = 1
        print(f"Você reservou um lugar na sala 1, fileira {fileira}, poltrona {assento}.")
    else:
        print("Este lugar já está reservado!")

def cancelar_reserva(sala,fileira, assento):
    if sala[fileira-1][assento-1] == 1:
        sala[fileira-1][fileira-1] = 0
        print(f"Você cancelou a reserva na sala 1, fileira {fileira}, poltrona {assento}.")
    else:
        print("Este lugar já está livre!")

def exibir_sala(sala):
    for fila in sala:
        print(" ".join(map(str, fila)))

sala = [[0]* 8 for fila in range(5)]

fileira = int(input("Qual fileira será a reserva? "))
poltrona = int(input("Qual o número do assento? "))
reservar(sala, fileira, poltrona)
#Mostra a sala atualmente 
print("MAPA DA SALA:")
exibir_sala(sala)

