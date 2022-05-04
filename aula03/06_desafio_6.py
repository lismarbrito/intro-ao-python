import colorama
# Você é a professora de Ciências e está lançando as notas das alunas.
# Você quer criar um sistema no qual suas alunas podem ver suas notas digitando o nome.
# As listas de alunas e notas se encontra abaixo. As notas podem variar de 0 a 100.
# Nessas listas, as notas estão na mesma ordem dos nomes, ou seja, a aluna no índice 4 tirou a nota no índice 4.


# Comece o programa perguntando o nome da aluna.


# Procure o nome digitado na lista de nomes e imprima uma mensagem com a nota que ela tirou.
# Notas abaixo de 60 devem ser impressas com a cor vermelha, e notas a partir de 90 devem ser
# impressas com a cor verde.
# Se o nome digitado não existir na lista, imprima uma mensagem de erro usando a cor vermelha.


colorama.init()
alunas = ['Adriana', 'Bárbara', 'Franciele', 'Laís', 'Maria', 'Nayara', 'Patrícia', 'Renata', 'Sarah', 'Thainá']
notas = [78, 57, 80, 98, 54, 89, 90, 100, 71, 85]

# def imprimir_colorido(nome, notas):
nome = input('Qual é o seu nome?\n')
posicao = alunas.index(nome)
if notas(posicao) < 60:
    print(colorama.Fore.RED + f'A aluna {nome} tirou {str(notas[posicao])} ')
    print(colorama.Style.RESET_ALL + notas)
    # elif nivel.lower() == 'aviso':
#         print(colorama.Fore.YELLOW + f'Aviso: ', end='')
#         print(colorama.Style.RESET_ALL + texto)
#     elif nivel.lower() == 'erro':
#         print(colorama.Fore.RED + f'Erro: ', end='')
#         print(colorama.Style.RESET_ALL + texto)
#     else:
#         print(colorama.Fore.RED + 'Erro interno - nível desconhecido de mensagem' + colorama.Style.RESET_ALL)

# print('A aluna ' + nome + ' tirou ' + str(notas[posicao]))

# print('índice | item')
# for i in alunas:
#     for j in notas:
#     if i == nome:
#     print(notas[j])
        # print(f' A aluna {nome.lower}   |  {item}')