import hashlib
 
class funcionario:
    def __init__(self, nome, email, cargo, lotacao, salario):
        self.__nome = nome
        self.__email = email
        self.__cargo = cargo
        self.__lotacao = lotacao
        self.__salario = salario
   
    def set_nome(self, nome):
        self.__nome = nome
   
    def get_nome(self):
        return self.__nome
   
    def set_email(self, email):
        self.__email = email
 
    def get_email(self):
        return self.__email
 
   
    def get_cargo(self):
        return self.__cargo
 
    def get_lotacao(self):
        return self.__lotacao
   
 
    def get_salario(self):
        return self.__salario
   
    def set_aumento(self):
        self.ativo = True
        print(f"Funcionario {self.__nome} solicitou um aumento")
 
    def detalhe_user(self):
        print(f"Nome: {self.__nome}")
        print(f"Email : {self.__email}")
        print(f"Cargo : {self.__cargo}")
        print(f"Lotação : {self.__lotacao}")
        print(f"Salario : {self.__salario}")
     
           
 
fun1 = funcionario( "asdasda", "sads@gmail.com", "funcionario", "213123123", "R$ 2.000,00")
 