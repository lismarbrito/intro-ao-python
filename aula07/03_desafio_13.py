import time

# Crie um decorator que calcule o tempo de execução de uma determinada função

def calcula_duracao(funcao):
    def wrapper():
        # Calcula o tempo de execução
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()

        # Formata a mensagem que será mostrada na tela
        print("[{funcao}] Tempo total de execução: {tempo_total}".format(
            funcao=funcao.__name__,
            tempo_total=str(tempo_final - tempo_inicial))
        )

    return wrapper

# Decora a função com o decorator
@calcula_duracao
def main():
    for n in range(0, 10000000):
        pass

# Executa a função main
main()

# Aplique seu decorator na função abaixo e veja quanto tempo a busca de um mesmo valor em um set e uma lista demoram para serem executadas
def  encontrar_item ( container , item ):
    devolver  item  em  recipiente

def  principal ():
    tamanho  =  1000000
    set_grande  =  set ( intervalo ( tamanho ))
    lista_grande  =  lista ( intervalo ( tamanho ))
    artigo  =  500399
    encontrar_item ( set_grande , item )
    encontrar_item ( lista_grande , item )

if  __name__  ==  '__main__' :
    principal ()

# Um Decorator permite adicionar qualquer comportamento antes ou depois de outra função.


# A sintaxe de uso do decorator é o @nome_do_decorator