class Calculadora:
    def adicionar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b


if __name__ == "__main__":
    calc = Calculadora()
    
    print("Calculadora:")
    print("1. Adicionar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")

    while True:
        try:
            opcao = int(input("Escolha uma opção (1/2/3/4) ou 0 para sair: "))
            if opcao == 0:
                break

            if opcao not in [1, 2, 3, 4]:
                print("Opção inválida. Tente novamente.")
                continue

            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))

            if opcao == 1:
                print(f"Resultado: {calc.adicionar(a, b)}")
            elif opcao == 2:
                print(f"Resultado: {calc.subtrair(a, b)}")
            elif opcao == 3:
                print(f"Resultado: {calc.multiplicar(a, b)}")
            elif opcao == 4:
                print(f"Resultado: {calc.dividir(a, b)}")

        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
