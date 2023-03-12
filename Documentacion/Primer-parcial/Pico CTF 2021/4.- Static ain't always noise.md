## Descripcion
Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/static)? This [BASH script](https://mercury.picoctf.net/static/7495259e963bd5b67d0fb8b616652618/ltdis.sh) might help!




## Solucion
``` bash 
┌──(kali㉿kali)-[~/Downloads]
└─$ ls -la 
total 251784
drwxr-xr-x  2 kali kali     4096 Mar 10 21:19 .
drwx------ 21 kali kali     4096 Mar 10 21:17 ..
-rw-r--r--  1 kali kali       34 Mar 10 20:34 flag
-rw-r--r--  1 kali kali 94838332 Feb 21 00:57 gitkraken-amd64.deb
-rw-r--r--  1 kali kali 93814424 Feb 15 21:39 google-chrome-stable_current_amd64.deb
-rw-r--r--  1 kali kali      785 Mar 10 21:19 ltdis.sh
-rw-r--r--  1 kali kali 69117910 Feb 21 01:12 obsidian_1.1.9_amd64.deb
-rw-r--r--  1 kali kali     8376 Mar 10 21:19 static
-rwxrwxrwx  1 kali kali    10936 Mar 10 20:39 warm
                                                                                      
┌──(kali㉿kali)-[~/Downloads]
└─$ chmod 777 ltdis.sh 
                                                                                      
┌──(kali㉿kali)-[~/Downloads]
└─$ ./ltdis.sh static 
Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets...
Any strings found in static have been written to static.ltdis.strings.txt with file of
                                                                                      
┌──(kali㉿kali)-[~/Downloads]
└─$ ls     
flag  gitkraken-amd64.deb  google-chrome-stable_current_amd64.deb  ltdis.sh  obsidian_
                                                                                      
┌──(kali㉿kali)-[~/Downloads]
└─$ strings static.ltdis.strings.txt | grep pico    
   1020 picoCTF{d15a5m_t34s3r_f6c48608}

```

## Bandera
picoCTF{d15a5m_t34s3r_f6c48608}

## Notas adicionales
|

## Referencias
