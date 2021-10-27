# importação das bibliotecas
import pandas as pd
from matplotlib import pyplot as plt
from time import sleep
from funcoes_mu import * # módulo de funções gerais
from funcoes_pandasmu import * # módulo de funções pandas

# variavel de iniciação do status do sistema
status = True

# saudação inicial da aplicação
resposta = saudacao()

if resposta.lower() == "sim":
  # criação do looping para exibição do menu e input do usuário
  while status:
    escolha = menu(["Total de atletas participantes",
                    "Total de participantes homens",
                    "Gráfico de porcentagem de atletas homens em relação ao total de atletas",
                    "Total de participantes mulheres",
                    "Gráfico de porcentagem de atletas mulheres em relação ao total de atletas",
                    "Total de participantes por esporte",
                    "Total de medalhas por país",
                    "Ranking por medalhas totais",
                    "País com mais medalhas de ouro",
                    "País com mais medalhas de prata",
                    "País com mais medalhas de bronze",
                    "País com menos medalhas de ouro",
                    "País com menos medalhas de prata",
                    "País com menos medalhas de bronze",
                    "Países com determinada quantidade de medalhas de ouro",
                    "Países com determinada quantidade de medalhas de prata",
                    "Países com determinada quantidade de medalhas de bronze",
                    "Gráfico de porcentagem de medalhas ganhas por um determinado país",
                    "Lista com esportes participantes",
                    "Lista de esportes com mais atletas homens que atletas mulheres",
                    "Lista de esportes com mais atletas mulheres que atletas homens",
                    "Lista de esportes com a mesma quantidade de atletas homens e mulheres",
                    "Quantidade de treinadores por país",
                    "País com a maior quantidade de treinadores",
                    "Quantidade de treinadores por esporte",
                    "Encerrar consulta"])
    if escolha == 1:
      print(separacao(76))
      total_atletas()
    elif escolha == 2:
      print(separacao(76))
      total_homens()
    elif escolha == 3:
      print(separacao(76))
      grafico_total_homens()
    elif escolha == 4:
      print(separacao(76))
      total_mulheres()
    elif escolha == 5:
      print(separacao(76))
      grafico_total_mulheres()
    elif escolha == 6:
      print(separacao(76))
      total_participantes_por_esporte()
    elif escolha == 7:
      print(separacao(76))
      total_medalhas_por_pais()
    elif escolha == 8:
      print(separacao(76))
      ranking_medalhas_totais()
    elif escolha == 9:
      print(separacao(76))
      mais_medalhas_ouro()
    elif escolha == 10:
      print(separacao(76))
      mais_medalhas_prata()
    elif escolha == 11:
      print(separacao(76))
      mais_medalhas_bronze()
    elif escolha == 12:
      print(separacao(76))
      menos_medalhas_ouro()
    elif escolha == 13:
      print(separacao(76))
      menos_medalhas_prata()
    elif escolha == 14:
      print(separacao(76))
      menos_medalhas_bronze()
    elif escolha == 15:
      print(separacao(76))
      quantidade_ouro()
    elif escolha == 16:
      print(separacao(76))
      quantidade_prata()
    elif escolha == 17:
      print(separacao(76))
      quantidade_bronze()
    elif escolha == 18:
      print(separacao(76))
      grafico_total_medalhas()
    elif escolha == 19:
      print(separacao(76))
      lista_esportes()
    elif escolha == 20:
      print(separacao(76))
      esportes_mais_homens()
    elif escolha == 21:
      print(separacao(76))
      esportes_mais_mulheres()
    elif escolha == 22:
      print(separacao(76))
      esportes_homens_iguais_mulheres()
    elif escolha == 23:
      print(separacao(76))
      treinadores_por_pais()
    elif escolha == 24:
      print(separacao(76))
      pais_mais_treinadores()
    elif escolha == 25:
      print(separacao(76))
      treinadores_por_esporte()
    elif escolha == 26:
      cabecalho("Encerrando o sistema!")
      break
    else:
      print("ERROR! Digite uma opção válida!")
    sleep(5)
    status = outra_consulta()
else:
  cabecalho("Encerrando o sistema!")