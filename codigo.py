def calcular_media(notas):
  quantidade = len(notas)
  soma = sum(notas)
  media = soma / quantidade
  print('O aluno tirou', media)
  return media

def verificar_aprovacao(media):
  if media >= 6:
    print('Aluno Aprovado')
  else:
    print('Aluno Reprovado')

calcular_media ([10, 9, 8, 7,])