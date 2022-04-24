# 1. Pergunte ao usuário em qual cidade e o estado em que ele(a) mora
cidade = input('Qual a sua cidade em que você mora?\n')
estado = input('E em qual estado você mora?\n')

# 2. Imprima uma mensagem diga a cidade em que o usuário mora. 
#    O nome da cidade deve estar todo em letras maiúsculas.
print("A cidade onde você mora é:", cidade.upper())


# 3. Imprima uma mensagem diga o estado em que o usuário mora. 
#    O nome do estado deve estar todo em letras maiúsculas.
#    Utilize uma forma de formatação de string diferente da que foi usada no item 2.
print(f'O estado onde você mora é: {estado.lower()}')