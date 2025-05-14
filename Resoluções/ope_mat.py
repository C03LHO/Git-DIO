num1 = int(input("Diginte o 1° numero: "))
num2 = int(input("Diginte o 2° numero: "))

operacao = input("Qual operação você deseja realizar(+, -, *, /): ")

if operacao == '+':
    print(num1 + num2)
elif operacao == '-':
    print(abs(num1 - num2))
elif operacao == '*':
    print(abs(num1 * num2))
elif operacao == "/":
    print(abs(num1 / num2))
else:
    print("Erro na operação")