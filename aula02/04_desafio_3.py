from datetime import datetime, timedelta

# Peça para o usuário digitar a data de seu próximo aniversário no formato brasileiro
aniversario_proximo = input('Digite a data de seu próximo aniversário (dd/mm/aa): ')
data_niver = datetime.strptime(aniversario_proximo, '%d/%m/%y').date()
# Imprima uma mensagem dizendo quantos dias faltam para o aniversário dele
hoje = datetime.now().date()
faltam_dias = str(abs((data_niver - hoje).days))
print('Faltam ' + faltam_dias + ' dias para seu próximo aniversário.')
# Pergunte ao usuário se ele(a) gosta de aniversário e salve a resposta
aniversario_gosta = input('Você gosta de aniversário? (sim/não) ')

# Pergunte ao usuário se ele(a) vai fazer festa e salve a resposta
aniversario_festa = input('Você vai fazer festa no seu aniversário? (sim/não) ')
# Imprima uma mensagem dizendo se o usuário vai ganhar presente ou não
# A regra é: o usuário só pode ganhar presente se gostar de aniversário e for fazer festa.
if (aniversario_gosta.lower() == 'sim' or aniversario_gosta.lower() == 's') and (aniversario_festa.lower() == 'sim' or aniversario_festa.lower() == 's'):
    print('Você vai ganhar presente no seu aniversário!!!')
else:
    print('Você não terá presente no seu aniversário.')

    
