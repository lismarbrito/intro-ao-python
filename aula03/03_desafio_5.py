# Crie uma lista com 60 números começando com o valor 1 e indo até o número 60 (ou seja, o número 60 deve estar na lista).
minha_lista = list(range(1, 61))
print("minha_lista: " + str(minha_lista))
print()

# Imprima todos os itens da sua lista de índice par. Imprima o índice e o item.
minha_lista2 = list(range(0, 61, 2))
print('índice | item')
print('------ | ----')
for i, item in enumerate(minha_lista2):
    print(f'   {i}   |  {item}')