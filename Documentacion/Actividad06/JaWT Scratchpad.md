## Descripcion

Check the admin scratchpad! `https://jupiter.challenges.picoctf.org/problem/61864/` or http://jupiter.challenges.picoctf.org:61864
## Pistas
What is that cookie?
Have you heard of JWT?


## Solucion
``` bash 

┌──(kali㉿kali)-[~/…/CiberSeguridad/Repositorio/notas-hacking/Utils]
└─$ john token -w=/usr/share/wordlists/rockyou.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 256/256 AVX2 8x])
Will run 6 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
ilovepico        (?)     
1g 0:00:00:01 DONE (2023-03-14 14:59) 0.9900g/s 7324Kp/s 7324Kc/s 7324KC/s iloveyokaos..ilovemymother@
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

```

![[JaWT.png]]
## Bandera
picoCTF{jawt_was_just_what_you_thought_1ca14548}

## Notas adicionales


## Referencias
https://jwt.io/