## Descripcion

To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with `nc jupiter.challenges.picoctf.org 29956`.

## Pistas

I hear python can convert things.
It might help to have multiple windows open.
## Solucion
```bash 
┌──(kali㉿kali)-[~]
└─$ nc jupiter.challenges.picoctf.org 29956                                        
Let us see how data is stored
socket
Please give the 01110011 01101111 01100011 01101011 01100101 01110100 as a word.
...
you have 45 seconds.....

Input:
socket
Please give me the  154 151 147 150 164 as a word.
Input:
light
Please give me the 74657374 as a word.
Input:
test
You've beaten the challenge
Flag: picoCTF{learning_about_converting_values_b375bb16}

```

``` python
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

```

``` bash 
Cadena binaria: 
01110011 01101111 01100011 01101011 01100101 01110100
socket
Cadena Octal: 
154 151 147 150 164
light
Cadena Hexadecimal: 
74657374
test
```

## Bandera
picoCTF{learning_about_converting_values_b375bb16}

## Notas adicionales
El script de python se encuentra en la carpeta de codigos 

## Referencias
