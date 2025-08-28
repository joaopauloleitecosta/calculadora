print("=== Calculadora Simples ===")

# Entrada de dados
try:
    num1 = float(input("Digite o primeiro número: ")) 
    num2 = float(input("Digite o segundo número: "))
except ValueError:
    print("Error: Você deve digitar apenas números.")
    exit()

# Escolha a operação
operacao = input("Escolha a operação (+, -, /, *): ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num1 != 0:
        resultado = num1 / num2
    else:
        "Erro: Divisão por zero!"
else:
    resultado = "Operação inválida!"

# Saída
print("Resultado: ", resultado)