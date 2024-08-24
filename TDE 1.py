from itertools import product  #importa a biblioteca de intertools para usar o cartesiano


def uniao():
  return conjunto1.union(conjunto2)  #funcao para calcular a uniao


def interseccao():
  return conjunto1.intersection(conjunto2)  #funcao para calcular a interseccao


def diferenca():
  return conjunto1.difference(conjunto2)  #funcao para calcular a diferenca


def cartesiano():
  return product(conjunto1, conjunto2)  #funcao para calcular o cartesiano


def diff_simetrica():
  return conjunto1.symmetric_difference(conjunto2)  #funcao para calcular
  #a diferenca simetrica


with open('exemplo1.txt',
          'r') as arquivo:  #abre o arquivo exemplo1.txt para leitura
  linhas = arquivo.readlines()
  numero_operacoes = int(
      (linhas[0]).strip())  #transforma a primeira linha do arquivo
  # em um inteiro

linha_auxiliar = 1  #vairavel auxiliar para armazenar a linha atual do arquivo
#e poder ler o arquivo todo

for operacao in range(numero_operacoes):  #loop para ler o arquivo baseado
  # na quantidade de operacoes
  operacao = linhas[linha_auxiliar].strip()
  conjunto1 = set(linhas[linha_auxiliar + 1].strip().split(','))
  conjunto2 = set(linhas[linha_auxiliar + 2].strip().split(','))

  if operacao == 'U':
    print("União: conjunto 1", conjunto1, "conjunto 2", conjunto2,
          ". Resultado: ", uniao())
  elif operacao == 'I':
    print("Intersecção: conjunto 1", conjunto1, "conjunto 2", conjunto2,
          ". Resultado: ", interseccao())

  elif operacao == 'D':
    print("Diferença: conjunto 1", conjunto1, "conjunto 2", conjunto2,
          ". Resultado: ", diferenca())

  elif operacao == 'C':
    print("Cartesiano: conjunto 1", conjunto1, "conjunto 2", conjunto2,
          ". Resultado: ", list(cartesiano()))

  elif operacao == 'S':
    print("Diferença simétrica: conjunto 1", conjunto1, "conjunto 2",
          conjunto2, ". Resultado: ", diff_simetrica())
  linha_auxiliar += 3
