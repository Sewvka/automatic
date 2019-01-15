from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


def encrypt_file_rsa(filename, publickey):
    # encryption RSA PublicKey1
    cipherrsa = PKCS1_OAEP.new(publickey)

    f = open(filename,'rb')
    TeXt = f.read();
    f.close()

    TeXt = cipherrsa.encrypt(TeXt)

    f = open(filename,'wb')
    f.write(bytes(TeXt));
    f.close()


def decrypt_file_rsa(filename, privatekey):
    # decryption RSA PrivateKey1
    cipherrsa = PKCS1_OAEP.new(privatekey)

    f = open(filename, 'rb')
    crypttext = f.read();
    f.close()

    crypttext = cipherrsa.decrypt(crypttext)

    f = open(filename, 'wb')
    f.write(bytes(crypttext));
    f.close()


if __name__ == '__main__':
    key = RSA.importKey(open('..\\keys\\KEYpub1.txt', 'rb').read())
    pkey = RSA.importKey(open('..\\keys\\KEYpr1.txt', 'rb').read())
    fname = '..\\RSA crypt\\TEXT.txt'
    decrypt_file_rsa(fname, pkey)
