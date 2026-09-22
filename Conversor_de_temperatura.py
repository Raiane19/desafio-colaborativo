# ============================================
# CONVERSOR DE TEMPERATURA
# Projeto: desafio-colaborativo-git
# ============================================


# ============================================
# NILTON ALVES
# Celsius ↔ Fahrenheit
# ============================================

def celsius_para_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# ============================================
# ARTHUR RIBEIRO
# Celsius ↔ Kelvin
# ============================================

def celsius_para_kelvin(celsius):
    return celsius + 273.15


def kelvin_para_celsius(kelvin):
    return kelvin - 273.15


# ============================================
# RAIANE DOS SANTOS
# Fahrenheit ↔ Kelvin
# ============================================

def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


def kelvin_para_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

while True:

    print("\n================================")
    print("     CONVERSOR DE TEMPERATURA")
    print("================================")

    print("1 - Celsius → Fahrenheit")
    print("2 - Fahrenheit → Celsius")
    print("3 - Celsius → Kelvin")
    print("4 - Kelvin → Celsius")
    print("5 - Fahrenheit → Kelvin")
    print("6 - Kelvin → Fahrenheit")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    # ========================================
    # NILTON ALVES
    # ========================================

    if opcao == "1":

        celsius = float(input("Digite a temperatura em Celsius: "))

        resultado = celsius_para_fahrenheit(celsius)

        print(f"Resultado: {resultado:.2f} °F")


    elif opcao == "2":

        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

        resultado = fahrenheit_para_celsius(fahrenheit)

        print(f"Resultado: {resultado:.2f} °C")


    # ========================================
    # ARTHUR RIBEIRO
    # ========================================

    elif opcao == "3":

        celsius = float(input("Digite a temperatura em Celsius: "))

        resultado = celsius_para_kelvin(celsius)

        print(f"Resultado: {resultado:.2f} K")


    elif opcao == "4":

        kelvin = float(input("Digite a temperatura em Kelvin: "))

        resultado = kelvin_para_celsius(kelvin)

        print(f"Resultado: {resultado:.2f} °C")


    # ========================================
    # RAIANE DOS SANTOS
    # ========================================

    elif opcao == "5":

        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

        resultado = fahrenheit_para_kelvin(fahrenheit)

        print(f"Resultado: {resultado:.2f} K")


    elif opcao == "6":

        kelvin = float(input("Digite a temperatura em Kelvin: "))

        resultado = kelvin_para_fahrenheit(kelvin)

        print(f"Resultado: {resultado:.2f} °F")


    # ========================================
    # SAIR
    # ========================================

    elif opcao == "0":

        print("Programa encerrado!")
        break


    else:

        print("Opção inválida! Tente novamente.")
