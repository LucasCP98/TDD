from Service.bytebank import Funcionario

lucas = Funcionario(nome='Lucas Costa Pereira',
                    data_nasmineto='12/02/1998',
                    salario=100000)

bonus = lucas.calcular_bonus()
print(bonus)


