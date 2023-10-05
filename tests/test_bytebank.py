import pytest

from Service.bytebank import Funcionario
from pytest import mark

'''
Muito importante, para que o Pytest reconheça que o metodo é um teste
a primeira para tem que começar com test_ ex: def test_idade.
O Arquivo .py sempre tem que começar com test 
* Caso queira rodar no terminal: pytest -v ou pytest
* Selecionar apenas um teste pelo terminal: pytest -v -k test_idade_retorna_25(nome metodo)
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
        funcionario_teste = Funcionario(nome='teste',
                                        data_nascimento=entrada,
                                        salario=100000)

        # When, Quando(Ação)
        resultado = funcionario_teste.idade()

        # Then, Então(Desfecho)
        assert resultado == esperado

    def test_sobronome_retorna_Pereira(self):
        # Given, Dado(Contexto)
        entrada = 'Lucas Costa Pereira'
        esperado = 'Pereira'
        funcionario_teste = Funcionario(nome=entrada,
                                        data_nascimento='12/02/1998',
                                        salario=100000)

        # When, Quando(Ação)
        resultado = funcionario_teste.sobrenome()

        # Then, Então(Desfecho)
        assert resultado == esperado

    # mar pytest: https://docs.pytest.org/en/7.1.x/how-to/mark.html#mark
    # @mark.skip  # EX: de mark padroes: Ele roda todos e com SKIP ele pula esse metodo test.
    def test_retirar_10_porcento_salario(self):
        # Given, Dado(Contexto)
        entrada = 100000
        esperado = 90000
        funcionario_teste = Funcionario(nome='teste',
                                        data_nascimento='12/02/1998',
                                        salario=entrada)

        # When, Quando(Ação)
        resultado = funcionario_teste.decrescimo_salario()

        # Then, Então(Desfecho)
        assert resultado == esperado

    # FIXME: Abaixo podemos ver @mark.calculo_bonus, uma opção de tag do pytest para demarca
    #   os metodos de test, por exemplo, existem dois testes que testam o mesmo metodo, no caso,
    #   o metodo que calcula o bonus para os funcionarios. A tag serve para facilitar na hora
    #   de rodar o teste do mesmo metodo.
    #   PARA RODAR NO TERMINAL: pytest -v -m calculo_bonus
    #   Rodando assim, ele irá rodar apenas os testes que possuem a tag que tem "calculo_bonus"
    #   * IMPORTANTE falar que o MARK do pytest, também tem mark padroes que podem ser usados,
    #   * para saber mais sobre digite no terminal: pytest --markers

    @mark.calculo_bonus
    def test_acrescimo_salarial_caso_menor_1000(self):
        # Given, Dado(Contexto)
        entrada = 1000
        esperado = 100
        funcionario_teste = Funcionario(nome='teste',
                                        data_nascimento='12/02/1998',
                                        salario=entrada)

        # When, Quando(Ação)
        resultado = funcionario_teste.calcular_bonus()

        # Then, Então(Desfecho)
        assert resultado == esperado

    @mark.calculo_bonus
    def test_acrescimo_salarial_quando_exception(self):
        # Pytest já tem uma ferramenta para o retorno de exception do metodo.
        with pytest.raises(Exception):
            # Given, Dado(Contexto)
            entrada = 100000
            # esperado = # Não precisa da varialvel esperado, pois entedesse que virá o exception
            funcionario_teste = Funcionario(nome='teste',
                                            data_nascimento='12/02/1998',
                                            salario=entrada)

            # When, Quando(Ação)
            resultado = funcionario_teste.calcular_bonus()

            # Then, Então(Desfecho)
            assert resultado  # == esperado, não precisa porque esperasse que venha o exception.

    # def test_str_todos_valores_do_funcionario(self):
    #     # Given, Dado(Contexto)
    #     nome, data_nascimento, salario = 'Teste', '12/02/1998', 1000
    #     esperado = f'Funcionario ({nome}, {data_nascimento}, {salario})'
    #     funcionario_teste = Funcionario(nome=nome, data_nascimento=data_nascimento, salario=salario)
    #
    #     # When, Quando(Ação)
    #     resultado = funcionario_teste.__str__()
    #
    #     # Then, Então(Desfecho)
    #     assert resultado == esperado
    #
    # def test_proprety_retorna_nome(self):
    #     # Given, Dado(Contexto)
    #     entrada = 'teste'
    #     esperado = 'teste'
    #     funcionario_teste = Funcionario(nome=entrada,
    #                                     data_nascimento='12/02/1998',
    #                                     salario=1000)
    #
    #     # When, Quando(Ação)
    #     resultado = funcionario_teste.nome
    #     # Then, Então(Desfecho)
    #     assert resultado == esperado

    # FIXME: Configurando ferramenta de cobertura
    #   instala o: pip install pytest-cov    ( Lembra do requirimets )
    #   ir no terminal: pytest --cov
    #   aparecerá uma lista: name: é o nome do arquivo, stmts: quantidade linha de codigo
    #   Miss: quantidade de linha que não foi testada, cover: porcentagem de quanto está testado.
    #   Caso, não esteja 100%, vamos no terminal: pytest --cov= (arquivo a testar ex: codigo)
    #   para rodar você coloca depois do =, a pasta que quer testar espaço, em seguida tests
    #   EX: pytest --cov=Service tests

    # FIXME: Garantindo cobertura total
    #   Para ver as linhas que não foram testadas, vamos no terminal.
    #   terminal: pytest --cov=Service tests --cov-report term-missing
    #   Irá aparecer uma nova aba: Missing com o numero da linha.
    #   * VOCÊ pode ignorar um teste que você oberserve que não é necessario, você vai
    #   criar um arquivo no meu diretorio principal um arquivo chamado de
    #   .coveragerc, é só olhar dentro dele que estará lá os arq ignorads

    # FIXME: Para vizualizar melhor a linhas erradas, vá no termianal:
    #   digite: terminal: pytest --cov=Service tests --cov-report html
    #   será criada uma pasta, dentro dela tem um arquivo chamado index.html
    #   clique com o botão direito, Open in, browser. Abrirá um arquvio
    #   na web, nele click nos 2 botoes [ ], aparecerá os erros.

