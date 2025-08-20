from abc import ABC, abstractclassmethod 
abstractproperty
from datetime import datetime


class Cliente:

    def __init__(self, endereço):
        self.endereço = endereço
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self,conta,transacao):
        transacao.registrar(conta)

class PessoaFisica(Cliente):

    def __init__(self, nome, cpf, endereço, data_nascimento):
        super().__init__(endereço)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self,numero,cliente):
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0
        self._agencia = "0001"
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia    
    
    @property
    def cliente(self):
        return self._cliente    
    
    @property
    def historico(self):
        return self._historico  
    
    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")    
            
        elif valor > 0:
            self._saldo -= valor
            print("\nSaque realizado com sucesso!")
            return True
        
        else:
            print("Operação falhou! Valor de saque inválido.")
            return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\nDepósito realizado com sucesso!")
        else:
            print("Operação falhou! Valor de depósito inválido.")
            return False
        
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500):
        super().__init__(numero, cliente)
        self._limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.
             transacoes if transacao['tipo'] == Saque.__name__]
        )
    
        execedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self.limite_saques

        if execedeu_limite:
            print("Operação falhou! Limite de saque excedido.")
        elif excedeu_saques:
            print("Operação falhou! Limite de saques diários excedido.")
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
            
        """
    
class Historico:
    def __init__(self):
        self.transacoes = []

    @property
    def transacoes(self):
        return self.transacoes

    def adicionar_transacao(self, transacao):
        self.transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao =conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
        
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
