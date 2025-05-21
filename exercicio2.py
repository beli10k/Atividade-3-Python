palavra = input("Digite uma palavra: ")
total = 0

for letra in palavra:
    if letra.lower() in "aeiou":
        total += 1

print("Total de vogais:", total)
