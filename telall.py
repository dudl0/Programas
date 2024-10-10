class Calculator:
    def evaluete_expression(self,expression):
        try:
            expression
            return expression
        except Exception:
            return 'Erro'

if __name__ == '__main__':
    calc = Calculator()
    print(calc.evaluete_expression('2+2'))
    print(calc.evaluete_expression('5*2'))
    print(calc.evaluete_expression('10/0')
