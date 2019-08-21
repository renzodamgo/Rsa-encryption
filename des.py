

p = int(input("p: "))
q = int(input("q: "))
d = int(input("d: "))

n = p*q
En = (p-1)*(q-1)
euler = 0

while True:
    mod = (d * euler) % En
    if mod == 1:
        break
    euler += 1

print("clave privada(", n, "," ,d,")" )
print("clave publica(", n, "," ,euler,")" )


word = input("word: ")
palabra = list(word)


while True:
    c = int(input("eor:"))
    enc = (c ** euler)%n
    print(enc)