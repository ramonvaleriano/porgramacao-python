from bytebank import Funcionario


milla = Funcionario("Milla Gabriela", "30/09/90", 30000)

print('Testando Classe Funcionario')
print(f"Funcionário: {milla.nome}")
print(f"Salario: {milla.salario}")
print(f"Idade: {milla.idade()}")