from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str):
        self.__valor = valor
        self.__descricao = descricao
 
    def setValor(self, valor):
        self.__valor = valor
    def setDescricao(self, descricao):
        self.__descricao = descricao

    def getValor(self):
        return self.__valor
    def getDescricao(self):
        return self.__descricao
    
    def resumo(self):
        print(f'Pagamento de R$ {self.getValor()}: {self.getDescricao()}')

    def validar_valor(self):
        if self.getValor() <= 0:
            print('valor incorreto')

    @abstractmethod
    def processar(self):
        pass

class CartaoCredito(Pagamento):
    def __init__(self, valor: float, descricao: str, numero: str, nome_titular: str, limite_disponivel: float):
        super().__init__(valor, descricao)
        self.__numero = numero
        self.__nome_titular = nome_titular
        self.__limite_disponivel = limite_disponivel

    def setNumero(self, numero: str):
        self.__numero = numero
    def setNomeTitular(self, nome_titular: str):
        self.__nome_titular = nome_titular
    def setLimiteDisponivel(self, limite_disponivel: float):
        self.__limite_disponivel = limite_disponivel

    def getNumero(self):
        return self.__numero
    def getNomeTitular(self):
        return self.__nome_titular
    def getLimiteDisponivel(self):
        return self.__limite_disponivel

    def processar(self):
        if self.getValor() > self.getLimiteDisponivel():
            print(f'Erro: Limite insuficiente no cartão {self.getNumero()}')
        else:
            self.setLimiteDisponivel(self.getLimiteDisponivel() - self.getValor())
            print(f'Pagamento aprovado no cartão {self.getNomeTitular()}. Limite restante: {self.getLimiteDisponivel()}')

class Pix(Pagamento):
    def __init__(self, valor: float, descricao: str, chave: str, banco: str):
        super().__init__(valor, descricao)
        self.__chave = chave
        self.__banco = banco

    def setChave(self, chave: str):
        self.__chave = chave
    def setBanco(self, banco: str):
        self.__banco = banco

    def getChave(self):
        return self.__chave
    def getBanco(self):
        return self.__banco

    def processar(self):
        if self.getValor() < 0:
            print('recusado errado')
        else:
            print(f'Pix enviado via banco {self.getBanco()} usando chave {self.getChave()}')

class Boleto(Pagamento):
    def __init__(self, valor: float, descricao: str, codigo_barras: str, vencimento: str):
        super().__init__(valor, descricao)
        self.__codigo_barras = codigo_barras
        self.__vencimento = vencimento

    def processar(self):
        print(f'Boleto gerado. Aguardando pagamento...')

def processar_pagamento(pagamento: Pagamento):
    pagamento.validar_valor()
    pagamento.resumo()
    pagamento.processar()

pagamentos = [
    Pix(150, "Camisa esportiva", "email@ex.com", "Banco XPTO"),
    CartaoCredito(400, "Tênis esportivo", "1234 5678 9123 4567", "Cliente X", 500),
    Boleto(89.90, "Livro de Python", "123456789000", "2025-01-10"),
    CartaoCredito(800, "Notebook", "9999 8888 7777 6666", "Cliente Y", 700),  # deve falhar
]

for i in pagamentos:
    processar_pagamento(i)