
# Binario
cadenaEntrada = input("Cadena binaria: \n")
lista = []
cadena = ""
lista = cadenaEntrada.split()

for i in lista:
    asscii = chr(int(i, 2))
    cadena += asscii
print(cadena)

# Octal
lista.clear()
cadenaEntrada = input("Cadena Octal: \n")
cadena = ""
lista = cadenaEntrada.split()

for i in lista:
    asscii = chr(int(i,8))
    cadena += asscii
print(cadena)

# Hexadecimal
lista.clear()
cadenaEntrada = input("Cadena Hexadecimal: \n")
cadena = ""
lista = cadenaEntrada.split()
byte = bytes.fromhex(cadenaEntrada)
asscii = byte.decode('ASCII')
print(asscii)