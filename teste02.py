def pertence_a_fibonacci(numero):
    fib_1, fib_2 = 0, 1

    if numero == fib_1 or numero == fib_2:
        return True

    while fib_2 < numero:
        fib_1, fib_2 = fib_2, fib_1 + fib_2

    return numero == fib_2

numero = int(input("Informe um número: "))

if pertence_a_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
