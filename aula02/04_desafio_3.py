from datetime import datetime, timedelta

# Peça para o usuário digitar a data de seu próximo aniversário no formato brasileiro
aniversario_proximo = input('Digite a data de seu próximo aniversário (dd/mm/aa): ')
# print(aniversario_proximo)
# Imprima uma mensagem dizendo quantos dias faltam para o aniversário dele
hoje = datetime.now().date()
# print(hoje.strftime('%d/%m/%y'))
faltam_dias = abs((aniversario_proximo - hoje).days)
print('Faltam ' + faltam_dias.strftime('%d/%m/%y') + ' para seu próximo aniversário.')
# Pergunte ao usuário se ele(a) gosta de aniversário e salve a resposta
aniversario_gosta = input('Você gosta de aniversário?')
# Pergunte ao usuário se ele(a) vai fazer festa e salve a resposta
aniversario_festa = input('Você vai fazer festa no seu aniversário?')
# Imprima uma mensagem dizendo se o usuário vai ganhar presente ou não
# A regra é: o usuário só pode ganhar presente se gostar de aniversário e for fazer festa.
if (aniversario_gosta == sim and aniversario_festa== sim):{
    print('Você vai ganhar presente no seu aniversário!!!')
} else {
    print(Vocênão terá presente no seu aniversário.)
}
    
