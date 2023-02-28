# Bandit Level 25 → Level 26


## Objetivo

Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not **/bin/bash**, but something else. Find out what it is, how it works and how to break out of it.

## Datos de acceso

bandit25
p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d

## Solucion
``` bash 

bandit25@bandit:~$ ssh -i bandit26.sshkey bandit26@localhost -p
2220
| |
| (_) | |__ \ / /
| |__
__ _ _ __
__| |_| |_
) / /_
| '_ \ / _` | '_ \ / _` | | __| / / '_ \'

--More--(83%)
v'
| |
| (_) | |__ \ / /
| |__
__ _ _ __
__| |_| |_
) / /_
| '_ \ / _` | '_ \ / _` | | __| / / '_ \
| |_) | (_| | | | | (_| | | |_ / /| (_) |
"~/text.txt" [readonly] 6L, 258B
:e /etc/bandit_pass/bandit26
c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1
~
~
~
~
"/etc/bandit_pass/bandit26" [readonly] 1L, 33B
:!q
| |
| (_) | |__ \ / /
| |__
__ _ _ __
__| |_| |_
) / /_
| '_ \ / _` | '_ \ / _` | | __| / / '_ \
| |_) | (_| | | | | (_| | | |_ / /| (_) |
Press ENTER or type command to continue
q
~
~
------------------------
Connection to localhost closed.
bandit25@bandit:~ exit
```

## Notas adicionales

| comado | descripcion |
|----------|-------------|
| ---| ---
|

## Referencias
