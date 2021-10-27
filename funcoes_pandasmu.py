# importação das bibliotecas
import pandas as pd
from matplotlib import pyplot as plt
from funcoes_mu import *

# criação dos dataframes
df_atletas = pd.read_excel("/content/documents/Athletes.xlsx")
df_treinadores = pd.read_excel("/content/documents/Coaches.xlsx")
df_entrada_genero = pd.read_excel("/content/documents/EntriesGender.xlsx")
df_medalhas = pd.read_excel("/content/documents/Medals.xlsx")
df_times = pd.read_excel("/content/documents/Teams.xlsx")

# renomeando colunas utilizadas
df_atletas.rename(columns={'Name': 'Nome', 'Discipline': 'Esporte'}, inplace = True)
df_treinadores.rename(columns={'Name': 'Nome', 'Discipline': 'Esporte'}, inplace = True)
df_entrada_genero.rename(columns={'Discipline': 'Esporte', 'Female': 'Feminino', 'Male': 'Masculino'}, inplace = True)
df_medalhas.rename(columns={'Team/NOC': 'Time/NOC', 'Gold': 'Ouro', 'Silver': 'Prata'}, inplace = True)
df_times.rename(columns={'Name': 'Nome', 'Discipline': 'Esporte'}, inplace = True)

# ========== FUNÇÕES PARA CONSULTA PANDAS ==========
# função que exibe total de atletas participantes
def total_atletas():
  total_atletas = df_atletas['Nome'].nunique()
  print(f"O total de atletas participantes é de {total_atletas}.")


# função que exibe total de participantes homens
def total_homens():
  total_homens = df_entrada_genero['Masculino'].sum()
  print(f"O total de participantes homens é de {total_homens}.")


# função que exibe total de participantes mulheres.
def total_mulheres():
  total_mulheres = df_entrada_genero['Feminino'].sum()
  print(f"O total de participantes mulheres é de {total_mulheres}.")


# função que exibe total de participantes por esporte
def total_participantes_por_esporte():
  df_entrada_genero['Total'] = df_entrada_genero['Feminino'] + df_entrada_genero['Masculino']
  print(df_entrada_genero[['Esporte', 'Total']])


# função que exibe total de medalhas por país
def total_medalhas_por_pais():
  df_medalhas['Total de Medalhas'] = df_medalhas['Ouro'] + df_medalhas['Prata'] + df_medalhas['Bronze']
  df_total_medalhas = df_medalhas.set_index('Rank')
  print(df_total_medalhas[['Time/NOC', 'Total de Medalhas']])


# função que exibe ranking por medalhas totais
def ranking_medalhas_totais():
  df_medalhas['Total de Medalhas'] = df_medalhas['Ouro'] + df_medalhas['Prata'] + df_medalhas['Bronze']  
  df_ranking_total = df_medalhas.sort_values(by=['Total de Medalhas'], ascending=False, ignore_index=True)
  print(df_ranking_total[['Total de Medalhas', 'Time/NOC']])


# função que exibe país com mais medalhas de ouro
def mais_medalhas_ouro():
  mais_ouro = df_medalhas[df_medalhas['Ouro'] == df_medalhas['Ouro'].max()]
  print(mais_ouro[['Time/NOC', 'Ouro']])


# função que exibe país com mais medalhas de prata
def mais_medalhas_prata():  
  mais_prata = df_medalhas[df_medalhas['Prata'] == df_medalhas['Prata'].max()]
  print(mais_prata[['Time/NOC', 'Prata']])


# função que exibe país com mais medalhas de bronze
def mais_medalhas_bronze():
  mais_bronze = df_medalhas[df_medalhas['Bronze'] == df_medalhas['Bronze'].max()]
  print(mais_bronze[['Time/NOC', 'Bronze']])


# função que exibe país com menos medalhas de ouro
def menos_medalhas_ouro():
  df_total_medalhas = df_medalhas.set_index('Rank')
  menos_ouro = df_total_medalhas[df_total_medalhas['Ouro'] == df_total_medalhas['Ouro'].min()]
  print(menos_ouro[['Time/NOC', 'Ouro']])


# função que exibe país com menos medalhas de prata
def menos_medalhas_prata():
  df_total_medalhas = df_medalhas.set_index('Rank')
  menos_prata = df_total_medalhas[df_total_medalhas['Prata'] == df_total_medalhas['Prata'].min()]
  print(menos_prata[['Time/NOC', 'Prata']])


# função que exibe país com menos medalhas de bronze
def menos_medalhas_bronze():
  df_total_medalhas = df_medalhas.set_index('Rank')
  menos_bronze = df_total_medalhas[df_total_medalhas['Bronze'] == df_total_medalhas['Bronze'].min()]
  print(menos_bronze[['Time/NOC', 'Bronze']])


# função que exibe lista com os esportes participantes
def lista_esportes():
  lista_esportes = df_entrada_genero['Esporte']
  print(lista_esportes)


# função que exibe lista de esportes com mais homens que mulheres
def esportes_mais_homens():
  esportes_mais_homens = df_entrada_genero[(df_entrada_genero['Masculino'] > df_entrada_genero['Feminino'])]
  lista_esportes_mais_homens = esportes_mais_homens.sort_values(by=['Masculino'], ascending=False)
  print(lista_esportes_mais_homens[['Esporte', 'Masculino', 'Feminino']])


# função que exibe lista de esportes com mais mulheres que homens
def esportes_mais_mulheres():
  esportes_mais_mulheres = df_entrada_genero[(df_entrada_genero['Feminino'] > df_entrada_genero['Masculino'])]
  lista_esportes_mais_mulheres = esportes_mais_mulheres.sort_values(by=['Feminino'], ascending=False)
  print(lista_esportes_mais_mulheres[['Esporte', 'Feminino', 'Masculino']])


# função que exibe lista da quantidade de treinadores por país
def treinadores_por_pais():
  qtd_treinadores = df_treinadores['Nome'].nunique()
  treinadores = df_treinadores['NOC'].value_counts()
  lista_treinadores = treinadores.to_dict()
  print(f"A quantidade total de treinadores é {qtd_treinadores}")
  for key, value in lista_treinadores.items():
    pais = key
    treinadores = value
    if value > 1:
      print(f"{pais} tem {value} treinadores")
    else:
      print(f"{pais} tem {value} treinador")


# função que exibe país com a maior quantidade de treinadores
def pais_mais_treinadores():
  treinadores = df_treinadores['NOC'].value_counts()
  lista_treinadores = treinadores.to_dict()
  for key, value in lista_treinadores.items():
    pais = key
    treinadores = value
    break
  print(f'O país com a maior quantidade de treinadores é {pais} com {treinadores} profissionais')


# função que exibe a quantidade de treinadores por esporte
def treinadores_por_esporte():
  print("A quantidade de treinadores por esportes é:")
  df_treinadoresU = df_treinadores.drop_duplicates()
  print(df_treinadoresU['Esporte'].value_counts())



# ========== FUNÇÕES EXTRAS ==========
# função para plotar gráfico de homens em relação ao total de atletas
def grafico_total_homens():
  soma_homens = df_entrada_genero['Masculino'].sum()
  total_atletas = df_entrada_genero['Feminino'].sum()
  atletas = [soma_homens, total_atletas]
  labels = ['Homens', 'Outro gênero']

  # nível de separabilidade entre as partes
  explode = (0.1, 0) 

  # definição das cores
  color = ['#48D1CC', '#D3D3D3']

  # definição do formato de visualização com saída em 1.1%%, sombras e a separação entre as partes para dar destaque à parte Homens
  plt.pie(atletas, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, colors=color)

  # criação de legendas e sua localização
  plt.legend(labels, loc=3)

  # plotar o gráfico em circulo
  plt.axis('equal')
  plt.show()


# função para plotar gráfico de mulheres em relação ao total de atletas
def grafico_total_mulheres():
  soma_mulheres = df_entrada_genero['Feminino'].sum()
  total_atletas = df_entrada_genero['Masculino'].sum()
  atletas = [soma_mulheres, total_atletas]
  labels = ['Mulheres', 'Outro gênero']

  # separabilidade
  explode = (0.1, 0) 

  # cores
  color = ['#F08080', '#D3D3D3']

  # formato de visualização
  plt.pie(atletas, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, colors=color)

  # legendas e sua localização
  plt.legend(labels, loc=3)

  # plotagem
  plt.axis('equal')
  plt.show()


# função que retorna países com a quantidade de ouro requisitada
def quantidade_ouro():
  outra_medalha = input("Deseja pesquisar por países medalhistas de ouro? (sim ou não) ")
  outra_medalha = verificando_string(outra_medalha)
  if outra_medalha.lower() == "sim":
    lista_qtd_medalhas = df_medalhas['Ouro'].unique()
    numero_medalhas = int(input("Digite o número de medalhas que procura: "))
    if numero_medalhas in lista_qtd_medalhas:
      medalhas_ouro = df_medalhas[df_medalhas['Ouro'] == numero_medalhas]
      print(medalhas_ouro[['Time/NOC', 'Ouro']])
    else:
      print(f"Nenhum país ganhou {numero_medalhas} medalha(s) de ouro")


# função que retorna países com a quantidade de ouro requisitada
def quantidade_prata():
  outra_medalha = input("Deseja pesquisar por países medalhistas de prata? (sim ou não) ")
  outra_medalha = verificando_string(outra_medalha)
  if outra_medalha.lower() == "sim":
    lista_qtd_medalhas = df_medalhas['Prata'].unique()
    numero_medalhas = int(input("Digite o número de medalhas que procura: "))
    if numero_medalhas in lista_qtd_medalhas:
      medalhas_prata = df_medalhas[df_medalhas['Prata'] == numero_medalhas]
      print(medalhas_prata[['Time/NOC', 'Prata']])
    else:
      print(f"Nenhum país ganhou {numero_medalhas} medalha(s) de prata")


# função que retorna países com a quantidade de ouro requisitada
def quantidade_bronze():
  outra_medalha = input("Deseja pesquisar por países medalhistas de bronze? (sim ou não) ")
  outra_medalha = verificando_string(outra_medalha)
  if outra_medalha.lower() == "sim":
    lista_qtd_medalhas = df_medalhas['Bronze'].unique()
    numero_medalhas = int(input("Digite o número de medalhas que procura: "))
    if numero_medalhas in lista_qtd_medalhas:
      medalhas_bronze = df_medalhas[df_medalhas['Bronze'] == numero_medalhas]
      print(medalhas_bronze[['Time/NOC', 'Bronze']])
    else:
      print(f"Nenhum país ganhou {numero_medalhas} medalha(s) de bronze")


# função para plotar gráfico do total de medalhas do país requisitado
def grafico_total_medalhas():
  opcao = input("Deseja ver o gráfico de medalhas de outro país? (sim ou não) ")
  opcao = verificando_string(opcao)
  if opcao.lower() == "sim":
    lista_paises = df_medalhas['Time/NOC'].unique()
    pais_escolhido = input("Digite o nome do país: ")
    if pais_escolhido in lista_paises:
      df_relativo = df_medalhas[df_medalhas['Time/NOC'] == pais_escolhido]
      gold = df_relativo['Ouro']
      silver = df_relativo['Prata']
      bronze = df_relativo['Bronze']    
      medalhas = [gold, silver, bronze]
      labels = ['Ouro', 'Prata', 'Bronze']
      explode = (0.1, 0, 0) 
      color = ['#FFD700', '#C0C0C0', "#B8860B"]
      plt.pie(medalhas, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, colors=color)
      plt.legend(labels, loc=3)
      plt.axis('equal')
      plt.show()

    else:
      print("O país digitado não foi encontrado na nossa base de dados :(")


# função que exibe lista de esportes com mesmo número de mulheres e homens
def esportes_homens_iguais_mulheres():
  esportes_mais_mulheres = df_entrada_genero[(df_entrada_genero['Feminino'] == df_entrada_genero['Masculino'])]
  lista_esportes_mais_mulheres = esportes_mais_mulheres.sort_values(by=['Feminino'], ascending=False)
  print(lista_esportes_mais_mulheres[['Esporte', 'Feminino', 'Masculino']])