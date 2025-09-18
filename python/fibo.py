def fibo(n):
    """Genera un generador con los primeros n números de Fibonacci."""
    a, b = 0, 1
    for _ in range(n + 1):
        yield a
        a, b = b, a + b

def write_list(values, filename: str = "toto.txt"):
    """Escribe la secuencia de Fibonacci en un archivo usando una lista."""
    with open(filename, "w") as f:
        for item in values:
            f.write(f"{item}\n")

rango = int(input("Ingresa tu rango aqui: "))
output = input("Ingresa un file name: ")

# Genera la lista de Fibonacci
fibo_list = list(fibo(rango))

# Escribe la lista en el archivo
write_list(fibo_list, output)
