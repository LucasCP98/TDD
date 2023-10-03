from datetime import date


class Funcionario:
    def __init__(self, nome, data_nasmineto, salario):
        self._nome = nome
        self._data_nasmineto = data_nasmineto
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        ano_atual = date.today().year
        data_nascimento_quebrada = self._data_nasmineto.split('/')[-1]
        return ano_atual - int(data_nascimento_quebrada)

    def sobrenome(self):
        nome_quebrado = self._nome.strip().split(' ')[-1]
        return nome_quebrado

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            valor = 0

        return valor

    def __str__(self):
        return f'Funcionario ({self._nome}, {self._data_nasmineto}, {self._salario})'
