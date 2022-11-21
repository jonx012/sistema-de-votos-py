candidatoA = input("Digite o candidatoA: ")
candidatoB = input("Digite o candidatoB: ")

candidatoA_votos = 0
candidatoB_votos = 0

candidatos = [candidatoA, candidatoB]

cont_de_pessoas = 0 

while cont_de_pessoas < 2:
 voto = input("Digite o seu candidato: ")
 if voto == candidatoA:
    print("Seu voto foi computado!!!")
    candidatoA_votos += 1
    cont_de_pessoas += 1
 elif voto== candidatoB:
   print("Seu voto foi computado!!!")
   candidatoB_votos += 1
   cont_de_pessoas += 1
 else:
   print('Candidato inserido está inválido')

if candidatoA_votos > candidatoB_votos:
   print(f"O {candidatoA} está eleito, com {candidatoA_votos} votos!")
elif candidatoB_votos > candidatoA_votos:
   print(f"O {candidatoB} está eleito, com {candidatoB_votos} votos!")
else:
   print("Irá ocorrer um 2° turno, a quantidade de votos foi igual!")

pergunta_ver_votos = 0

while pergunta_ver_votos == 0:
   print("Deseja ver o número de votos?")
   ver_votos = input("Digite sim ou nao: ").upper()
   if ver_votos == "SIM":
      print(candidatoA, '=', candidatoA_votos, 'votos.')
      print(candidatoB, '=', candidatoB_votos, 'votos.')  
      exit()
   elif ver_votos == 'NAO' or ver_votos == 'NÃO':
      exit()
   else:
      print('error') 
