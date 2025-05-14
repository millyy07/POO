class  contaBancaria:
     def __init__(self, titular, saldo):
        self.titular = titular # público
        self.__saldo = saldo   # privado

        def get_saldo(self):
            return self.__saldo

        def set_saldo(self, saldo):
            self.__saldo = saldo


conta = contaBancaria("emilly" , 60.0)

print(f"saldo : {conta.__saldo}")
conta.set_saldo(1000.0)
print(f"novo saldo: {conta.get_saldo()}")
