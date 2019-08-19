

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

end_word = ""
dec_word = ""
for caracter in palabra:
    c = ord(caracter)
    encrypt = (c ** euler)%n
    end_word += chr(encrypt)
    
   
print (end_word)


for caracter in end_word:
    c = ord(caracter)
    decrypt = (c ** d)%n    
    dec_word += chr(decrypt)

print (dec_word)

