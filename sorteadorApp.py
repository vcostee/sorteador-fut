import random

def sortearTimes(stringInput):
  listaJogadores = []
  texto = ""

  stringJogadores = stringInput
  stringJogadores = stringJogadores.replace(" ", "")
  stringPorNivel = stringJogadores.split("/")
  xPorTime = len(stringPorNivel)
  print('\n')

  nivel = xPorTime
  for spn in stringPorNivel:
    jogadores_aux = spn.split(",")
    for j_aux in jogadores_aux:
      listaJogadores.append([j_aux, nivel])
    nivel -= 1


  texto += '_*---------- SORTEIO FUT INIMIGOS DA BOLA ----------*_'
  texto += '\n\n'

  i_time = 1

  while i_time <= len(stringPorNivel[0].split(",")):
    jogador = ""
    nivel = xPorTime
    pos = 1
  
    texto += f'*TIME {i_time}* \n'
    while nivel > 0 :
      lista_aux = [j for j in listaJogadores if j[1] == nivel]
      jogador = random.choice(lista_aux)
      texto += f'*{pos} -* ' + jogador[0] + '\n'
      nivel -= 1
      pos += 1
      listaJogadores.remove(jogador)
    
    texto += '\n'
    i_time += 1
  return texto
