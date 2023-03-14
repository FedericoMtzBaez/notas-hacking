
## Descripcion

Can you make sense of this file?
## Pistas

Multiple decoding is always good.

## Solucion
``` bash 

┌──(kali㉿kali)-[~/…/CiberSeguridad/Repositorio/notas-hacking/Utils]
└─$ cat enc_flag 
VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVh
RmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNk
MlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVW
VkpEVGxaYVdFMVhSbFZhTTBKWVZGVm9RMDFHV1hoWGJFNW9DbUpXUmpOVVZsWlhWakpHZEdWRlZs
aGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg==
                                                                                                                                                                                
┌──(kali㉿kali)-[~/…/CiberSeguridad/Repositorio/notas-hacking/Utils]
└─$ cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d
picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_1bfa7005}

```

## Bandera
picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_1bfa7005}

## Notas adicionales
|

## Referencias