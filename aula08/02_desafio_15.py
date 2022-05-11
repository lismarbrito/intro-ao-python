# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
class Carro:
    def __init__(self, cor, modelo): 
        self.ligado = False
        self.cor = cor
        self.velocidade = 1
        self.velocidade_min = 0
        self.velocidade_max = 150
        self.modelo = modelo
    def ligar(self):
            self.ligado = True
    def desligar(self):
            self.ligado = False    

# Crie uma instância da classe carro.
carro_passeio = Carro()
carro_trabalho = Carro()
    

# Faça o carro "andar" utilizando os métodos da sua classe.
    def acelerar_carro(self):
        if not self.ligado:  #testa se a tv esta ligada
            return

        if self.velocidade < self.velocidade_max:
            self.velocidade += 1

# Faça o carro "parar" utilizando os métodos da sua classe.

    def reduzir_carro(self):
        if not self.ligado:
            return

        if self.velocidade > self.velocidade_max:
            self.velocidade += 1

    
    
   
    
    

    
        
    def aumentar_volume(self):
        if not self.ligada: #testa se a tv esta ligada
            return

        if self.volume < self.volume_max:
            self.volume += 10

    def reduzir_volume(self):
        if not self.ligada: #testa se a tv esta ligada
            return

        if self.volume > self.volume_min:
            self.volume -= 10
    # retorna uma string
    def __str__(self) -> str: 
        return f'Televisao - ligada {self.ligada} - canal {self.canal} - volume {self.volume}'