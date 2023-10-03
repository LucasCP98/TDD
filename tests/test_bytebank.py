from Service.bytebank import Funcionario

'''
Muito importante, para que o Pytest reconheça que o metodo é um teste
a primeira para tem que começar com test_ ex: def test_idade.
O Arquivo .py sempre tem que começar com test 
Caso queira rodar no terminal: pytest -v ou pytest
'''


class TestClass:
    # FIXME: Teste feito ultizando o método Given-When-Then
    #  * Dado(Contexto) Tenho dinheiro e quero comprar uma camisa.
    #  * Quando(Ação) Acesso o Site que contém a camisa.
    #  * Então(Desfecho) Compro a camisa.
    def test_idade_retorna_25(self):
        # Given, Dado(Contexto)
        entrada = '12/02/1998'
        esperado = 25
        funcionario_teste = Funcionario(nome='teste', data_nasmineto=entrada, salario=1000)

        # When, Quando(Ação)
        resultado = funcionario_teste.idade()

        # Then, Então(Desfecho)
        assert resultado == esperado

    def test_sobronome_retorna_Pereira(self):
        # Given, Dado(Contexto)
        entrada = 'Lucas Costa Pereira'
        esperado = 'Pereira'
        funcionario_teste = Funcionario(nome=entrada, data_nasmineto='12/02/1998', salario=1000)

        # When, Quando(Ação)
        resultado = funcionario_teste.sobrenome()

        # Then, Então(Desfecho)
        assert resultado == esperado
