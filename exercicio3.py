numeros = []

for i in range(3):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

multiplicados = [n * 2 for n in numeros]

print("Números originais:", numeros)
print("Números multiplicados por 2:", multiplicados)

soma = sum(numeros)
print("Soma dos números originais:", soma)
