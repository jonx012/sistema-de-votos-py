import os

#cadastrar-candidatos
candidatoA = input("Digite o candidatoA: ").upper()
numero_candidatoA = input(f"Digite o número do candidato {candidatoA}: ")
candidatoB = input("Digite o candidatoB: ").upper()
numero_candidatoB = input(f"Digite o número do candidato {candidatoB}: ")

candidatos_list = {candidatoA : numero_candidatoA, candidatoB : numero_candidatoB, "NULO": "00"}
   
fazer_votacao = 0

while fazer_votacao == 0:
   comecar_ou_nao = input("Deseja fazer a votação? [S/N]: ").upper()
   if comecar_ou_nao == "S":
      os.system('cls' if os.name == 'nt' else 'clear')
      fazer_votacao += 1
   elif comecar_ou_nao == "N":
      exit("Até breve...")
   else:
      print(f"error\n")

#fazer-votacao
total_de_votos = 5
cont_de_votos = 0 

candidatoA_votos = 0
candidatoB_votos = 0
nulo_votos = 0
branco_votos = 0

while cont_de_votos < total_de_votos:
 print(f"\n{candidatoA} = {numero_candidatoA}\n{candidatoB} = {numero_candidatoB}")
 print(f"Nulo = 00\nBranco = Branco\n")
 voto = input("Digite o seu candidato: ").upper()
 if voto == candidatos_list[candidatoA]:
    print(f"Seu voto foi computado!!!\n")
    candidatoA_votos += 1
    cont_de_votos += 1
 elif voto == candidatos_list[candidatoB]:
   print(f"Seu voto foi computado!!!\n")
   candidatoB_votos += 1
   cont_de_votos += 1
 elif voto == candidatos_list["NULO"]:
   print(f"Seu voto foi computado!!!\n")
   nulo_votos += 1
   cont_de_votos += 1
 elif voto == "BRANCO":
   print(f"Seu voto foi computado!!!\n")
   branco_votos += 1
   cont_de_votos += 1
 else:
   print(f"Candidato inserido está inválido\n")

#calcular-%-dos-votos
candidatoA_votos_porcentagem = int((candidatoA_votos / total_de_votos)*100)
candidatoB_votos_porcentagem = int((candidatoB_votos / total_de_votos)*100)
nulo_votos_porcentagem = int((nulo_votos / total_de_votos)*100)
branco_votos_porcentagem = int((branco_votos / total_de_votos)*100)

#resultado-da-votacao
if candidatoA_votos > candidatoB_votos:
   print(f"O {candidatoA} está eleito, com {candidatoA_votos_porcentagem}% dos votos!\n")
elif candidatoB_votos > candidatoA_votos:
   print(f"O {candidatoB} está eleito, com {candidatoB_votos_porcentagem}% dos votos!\n")
else:
   print(f"Irá ocorrer um 2° turno, a quantidade de votos foi igual!\n")

#mostrar-ou-nao-os-votos
pergunta_ver_votos = 0

while pergunta_ver_votos == 0:
   ver_votos = input(f"Deseja ver o número de votos? [S/N]: ").upper()
   if ver_votos == "S":
      print(f"\n{candidatoA} = {candidatoA_votos} voto(s), ou seja, {candidatoA_votos_porcentagem}% dos votos.")
      print(f"{candidatoB} = {candidatoB_votos} voto(s), ou seja, {candidatoB_votos_porcentagem}% dos votos.")
      print(f"NULO = {nulo_votos} voto(s), ou seja, {nulo_votos_porcentagem}% dos votos.")
      print(f"BRANCO = {branco_votos} voto(s), ou seja, {branco_votos_porcentagem}% dos votos.")
      exit()
   elif ver_votos == "N":
      exit()
   else:
      print(f'error\n') 
