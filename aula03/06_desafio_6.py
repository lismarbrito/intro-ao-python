import colorama
# Você é a professora de Ciências e está lançando as notas das alunas.
# Você quer criar um sistema no qual suas alunas podem ver suas notas digitando o nome.
# As listas de alunas e notas se encontra abaixo. As notas podem variar de 0 a 100.
# Nessas listas, as notas estão na mesma ordem dos nomes, ou seja, a aluna no índice 4 tirou a nota no índice 4.
alunas = ['Adriana', 'Bárbara', 'Franciele', 'Laís', 'Maria', 'Nayara', 'Patrícia', 'Renata', 'Sarah', 'Thainá']
notas = [78, 57, 80, 98, 54, 89, 90, 100, 71, 85]

# Comece o programa perguntando o nome da aluna.
nome = input('Qual é o seu nome?\n')

# Procure o nome digitado na lista de nomes e imprima uma mensagem com a nota que ela tirou.
# Notas abaixo de 60 devem ser impressas com a cor vermelha, e notas a partir de 90 devem ser
# impressas com a cor verde.
# Se o nome digitado não existir na lista, imprima uma mensagem de erro usando a cor vermelha.
colorama.init()
if nome not in alunas:
    print(colorama.Fore.RED + 'Erro - o nome ' + nome + ' não está na lista!')
    print(colorama.Style.RESET_ALL)


posicao = alunas.index(nome)    
if notas[posicao] < 60:
    print('A aluna ' + nome + ' tirou ' + colorama.Fore.RED + str(notas[posicao]))
    print(colorama.Style.RESET_ALL)
elif notas[posicao] >= 90:
    print('A aluna ' + nome + ' tirou ' + colorama.Fore.GREEN + str(notas[posicao]))
    print(colorama.Style.RESET_ALL)
else:
    print('A aluna ' + nome + ' tirou ' + str(notas[posicao]))