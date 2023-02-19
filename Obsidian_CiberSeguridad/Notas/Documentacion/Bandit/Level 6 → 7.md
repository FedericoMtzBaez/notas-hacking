# Bandit Level 6 → Level 7


## Objetivo

The password for the next level is stored **somewhere on the server** and has all of the following properties:

-   owned by user bandit7
-   owned by group bandit6
-   33 bytes in size

## Datos de acceso

bandit6
P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU

## Solucion
``` bash

bandit6@bandit:/$ cat ./var/lib/dpkg/info/bandit7.password
z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S


```

## Notas adicionales

| comado | descripcion |
|----------|-------------|
| ---| ---
|

## Referencias
