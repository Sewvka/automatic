from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

privatekey = RSA.generate(2048)
f = open('c:\qwertyui\\KEYpr1.txt','wb')        #приватный ключ 1
f.write(bytes(privatekey.exportKey('PEM'))); f.close() #11 11 11

publickey = privatekey.publickey() #
f = open('c:\qwertyui\\KEYpub1.txt','wb')        #публичный ключ 1
f.write(bytes(publickey.exportKey('PEM'))); f.close() #12 12 12