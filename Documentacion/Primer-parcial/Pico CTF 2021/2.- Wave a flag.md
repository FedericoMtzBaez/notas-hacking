## Descripcion

## Pistas
Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/cfea736820f329083dab9558c3932ada/warm) has extraordinarily helpful information...


## Solucion
``` bash 
┌──(kali㉿kali)-[~/Downloads]
└─$ ./ warm
zsh: permission denied: ./

┌──(kali㉿kali)-[~/Downloads]
└─$ ls -la
total 251768
drwxr-xr-x  2 kali kali     4096 Mar 10 20:40 .
drwx------ 21 kali kali     4096 Mar 10 20:34 ..
-rw-r--r--  1 kali kali       34 Mar 10 20:34 flag
-rw-r--r--  1 kali kali 94838332 Feb 21 00:57 gitkraken-amd64.deb
-rw-r--r--  1 kali kali 93814424 Feb 15 21:39 google-chrome-stable_current_amd64.deb
-rw-r--r--  1 kali kali 69117910 Feb 21 01:12 obsidian_1.1.9_amd64.deb
-rw-r--r--  1 kali kali    10936 Mar 10 20:39 warm
                                                                                      
┌──(kali㉿kali)-[~/Downloads]
└─$ chmod 777 warm  
                                                                                      
┌──(kali㉿kali)-[~/Downloads]
└─$ ./warm 
Hello user! Pass me a -h to learn what I can do!
                                                                                      
┌──(kali㉿kali)-[~/Downloads]
└─$ ./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_30e77291}

```

## Bandera
picoCTF{b1scu1ts_4nd_gr4vy_30e77291}

## Notas adicionales
|

## Referencias
