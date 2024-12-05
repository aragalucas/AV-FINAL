from funcionario import Funcionario
funcionario = Funcionario()
funcionario.nome = input("nome: ")
funcionario.email  = input("email: ")
funcionario.salario = input("salario: ")
funcionario.endereco = input("endereço: ")
salariofinal = funcionario.salario
print("\ndados do funcionario")
print(f"nome: {funcionario.nome}")
print(f"email: {funcionario.email}")
print(f"salario: {funcionario.salario}")
print(f"endereço: {funcionario.endereco}")
print(f"salario final: {salariofinal}")