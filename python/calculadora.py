# Código feito para acompanhar o vídeo sobre básicos de programação, disponível em: "link do video aqui"

def add():

    a = int(input("Digite o primeiro número: ")) # Código para receber um número do usuário
    b = int(input("Digite o segundo número: "))

    print(f"Resultado: {a + b}")



def sub():

    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    print(f"Resultado: {a - b}")



def mult():

    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    print(f"Resultado: {a * b}")



def div():

    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    if b == 0:  # Verifica se o divisor é zero para evitar divisões inválidas
        print("Divisão por zero")

    else:
        print(f"Resultado: {a / b}")



def print_menu():
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")



def main():

    print_menu()
    option = input("Escolha uma opção: ")

    while option != "0": # loop para manter o programa rodando até que o usuário escolha a opção de sair

        if option == "1":
            add()

        elif option == "2":
            sub()

        elif option == "3":
            mult()

        elif option == "4":
            div()

        else:
            print("Opção inválida")

        print_menu()
        option = input("Escolha uma opção: ")



main()