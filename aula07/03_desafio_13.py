import time

# Crie um decorator que calcule o tempo de execução de uma determinada função

def calcular_duracao(funcao):
    def wrapper():
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()

        print("Tempo total de execução da função: {tempo_total}".format(
            funcao=funcao.__name__,
            tempo_total=str(tempo_final - tempo_inicial))
        )

    return wrapper



# Aplique seu decorator na função abaixo e veja quanto tempo a busca de um mesmo valor em um set e uma lista demoram para serem executadas
def encontrar_item(container, item):
    return item in container

@calcular_duracao
def main():
    tamanho = 1000000
    set_grande = set(range(tamanho))
    lista_grande = list(range(tamanho))
    item = 500399
    encontrar_item(set_grande, item)
    encontrar_item(lista_grande, item)

if __name__ == '__main__':
    main()