# Código feito para acompanhar o vídeo sobre básicos de programação, disponível em: "link do video aqui"

def add():

    a = int(input("Digite o primeiro número: ")) # Código para receber um número do usuário
    b = int(input("Digite o segundo número: "))

    resultado = a + b # Código para somar os dois números

    print(f"Resultado: {resultado}")



def sub():

    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    resultado = a - b # Código para subtrair os dois números

    print(f"Resultado: {resultado}")



def mult():

    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    resultado = a * b # Código para multiplicar os dois números

    print(f"Resultado: {resultado}")



def div():

    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    if b == 0:  # Verifica se o divisor é zero para evitar divisões inválidas
        print("Divisão por zero")

    else:
        resultado = a / b # Código para dividir os dois números

        print(f"Resultado: {resultado}")



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