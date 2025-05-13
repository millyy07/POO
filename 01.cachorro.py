class cachorro:
    #inicializador
    def __init__(self, nome, idade, raca, comida):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.comida = comida
        self.acordado = false
        self.feliz = false
        self.energia = 100
    
    def __str__(self):
        return f"nome: {self.nome}, raça: {self.raca}, idade: {self.idade}, comida: {self.comida} disponível, acordado: {self.acordado}, feliz: {self.feliz}, energia: {self.energia}"

    #metodos
    def comer(self):
        if self.comer >= quantidade:
            self.comida -= quantidade
            self.feliz = true
            print(f"")

    def acordar(self):
        print(f"{self.nome} está acordado!")

    def dormir(self): 
        self.energia = 100
        self.acordado = false
        print(f"{self.nome} está dormindo!")   

    def brincar(self):
        if self.acordado:
            if self.energia >= 20:
                self.feliz = true
                self.energia -= 20
                print(f"{self.nome} etá brincando e está feliz!")
            else:
                print(f"{self.nome} está sem energia e não pode brincar")
        else:
            print(f"{self.nome} está dormind, não pode brincar!")

    def  ignorar(self):
        self.feliz = false
        print(f"{self.nome} foi  ignorado e está triste.")

    def latir(self):
        if self.acordado:
            print(f"{self.nome} está  latindo! woof woof!")
        else:
            print(f"{self.nome} está dormindo e não pode latir!")       

            
             

