class carros():
    def __init__(self, modelo,cor, ano):
        self.modelo = modelo
        self.cor = cor 
        self.ano = ano
        
        
    def mostrar_modelo(self):
        return self.modelo
    def mostrar_cor(self):
        return self.cor
    def mostrar_ano(self):
        return self.ano
        
carro = carros("prisma", "preto", "2013")

print(carro.mostrar_modelo())

print(carro.mostrar_cor())


print(carro.mostrar_ano())
        
