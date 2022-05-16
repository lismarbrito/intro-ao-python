# Dado um arquivo de entrada, escreva um programa que leia o conteudo do arquivo para uma string,
# e escreva um outro arquivo de saída que imprima o texto ao contrário.
# Exemplo de entrada: Oi mulheres maravilhosas do curso de Python do ConstruDelas!
# Exemplo de saída: !saleDurtsnoC od nohtyP ed\nosruc od sasohlivaram serehlum iO

arquivo_entrada = 'entrada_desafio_11.txt'
with open(arquivo_entrada, 'r') as arquivo01:
    text = arquivo01.read()
    print(text)

arquivo_saida = 'entrada_desafio_11.txt'
with open(arquivo_saida, 'w') as arquivo02:
    arquivo02.write(text[::-1])

