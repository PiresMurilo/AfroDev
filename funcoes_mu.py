# ========== FUNÇÕES NECESSÁRIAS ==========

# função que verifica se é o valor é uma string válida
def verificando_string(valor):
  while valor.isnumeric():
      print("ERROR!")
      valor = input("Por favor, digite novamente: ")
  return valor


# função que imprime separação
def separacao(tamanho):
  return '-' * tamanho


# centralização do cabeçalho do menu
def cabecalho(texto):
  print(separacao(76))
  print(texto.center(70))
  print(separacao(76))

# 
def outra_consulta():
  resposta = input("Deseja realizar outra consulta? ")
  verificando_string(resposta)
  if resposta.lower() == "sim":
    return True
  else:
    return False

# saudação inicial do sistema
def saudacao():
  cabecalho("SISTEMA DE ANÁLISE - TOKYO 2021")
  genero = input("Nos diga por qual gênero prefere ser tratadx (masculino, feminino ou neutro): ")
  verificando_string(genero)
  if genero.lower() == "masculino":
      artigo = "o"
  elif genero.lower() == "feminino":
      artigo = "a"
  else:
      artigo = "x"
  print(f"Seja bem-vind{artigo} à plataforma de consultas sobre os Jogos Olímpicos Tokyo 2021!")
  ini = input(f"Você sabia que a Tokyo 2021 bateu recordes em números de eventos, países participantes e modalidades esportivas? ")
  ini2 = input(f"E sabia que, com aumento de 2,9% comparado a Rio 2016, essa foi a Olimpíada mais próxima da igualdade de gênero entre os atletas? ")
  resposta = input(f"Deseja consultar mais informações sobre a Tokyo 2021? (sim ou não) ")
  verificando_string(resposta)
  return resposta


# função que imprime o menu e retorna opção escolhida
def menu(lista_menu):
  print("\n")
  cabecalho("Menu")
  numerador = 1
  for item in lista_menu:
    print(f"{numerador}. {item}")
    numerador += 1
  print(separacao(76))  
  opcao = int(input("Digite o número correspondente à consulta desejada: "))
  return opcao