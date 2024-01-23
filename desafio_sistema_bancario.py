#============================================
# Versão do desafio DIO Sistema Bancário
# Desenvolvido por Nei Freitas em 23/01/2024
#============================================

from datetime import date

menu = """
========================================
Selecione a operação desejada:
========================================

[D]epositar
[S]acar
[E]xtrato
[F]echar 

=> """

# Iniciando as variáveis
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao.upper() == "D":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            if saldo < 0:
                saldo += valor
                limite += abs(saldo - valor)
                extrato += f"{date.today()} - Depósito\t\tR$ {valor:.2f}\n"
            else:    
                saldo += valor
                extrato += f"{date.today()} - Depósito\t\tR$ {valor:.2f}\n"
        else:
            print("O valor do depósito deve ser maior que zero!")
            continue

    elif opcao.upper() == "S":
        valor = float(input("Informe o valor a ser sacado: "))

        # Verifica condição para saque
        excedeu_saldo = valor > saldo + limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if valor > 0:
            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente!")
            else:
                if not excedeu_saque:
                    if saldo <= 0:
                        saldo -= valor
                        limite -= valor
                        extrato += f"{date.today()} - Saque\t\tR$ {valor:.2f}\n"
                        numero_saques += 1
                    else:
                        saldo -= valor
                        extrato += f"{date.today()} - Saque\t\tR$ {valor:.2f}\n"
                        numero_saques += 1
                else:
                    print("Operação falhou! Você atingiu o número de saques permitidos no período!")
        else:
            print("O valor do saque deve ser maior que zero!")
            continue

    elif opcao.upper() == "E":
        if extrato:
            print("================ EXTRATO CONTA CORRENTE ==================\n")
            print(extrato)
            print("==========================================================")
            print(f"Saldo atual:\t\t\tR$ {saldo:.2f}")
            print(f"Limite disponível:\t\tR$ {limite:.2f} ")
            print(f"Número de saques realizados:\t{numero_saques}")
            print("==========================================================")
        else:
            print("================ EXTRATO CONTA CORRENTE ==================")
            print("Não houveram movimentações no período!")
            print("==========================================================")
            print(f"Limite disponível: {limite:.2f} ")
            print(f"Número de saques realizados: {numero_saques}")
            print("==========================================================")

    elif opcao.upper() == "F":
        exit()
