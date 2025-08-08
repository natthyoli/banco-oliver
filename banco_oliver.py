print("\nCofrinho Winona:")
print("[1] Adicionar dinheiro")
print("[2] Sacar")
print("[3] Transferir")

escolha_operacao = int(input("Escolha a transação a realizar: "))
salario = float(input("Digite o seu salário: "))

if escolha_operacao == 1:
    valor_adicionar = float(input("Valor R$ que será adicionado: "))
    if valor_adicionar >= 100:
        print(f"Você adicionou R${valor_adicionar:.2f}")
    else:
        print("Valor insuficiente para adicionar")
    print(f"O saldo atual do seu salário é R${salario + valor_adicionar:.2f}")

elif escolha_operacao == 2:
    valor_subtrair = float(input("Valor do saque: "))
    print(f"O saldo atual do seu salário é R${salario - valor_subtrair:.2f}")

elif escolha_operacao == 3:
    valor_transferencia = float(input("Digite o valor da transferência: "))
    if valor_transferencia <= 500:
        print(f"O valor da transferência é R${valor_transferencia:.2f}. O saldo do salário é R${salario - valor_transferencia:.2f}")
    else:
        print("Valor não permitido para transferência")

else:
    print("Opção inválida. Tente novamente.")
