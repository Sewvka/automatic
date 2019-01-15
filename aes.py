import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

BLOCK_SIZE=32

def get_key(filename):
    f = open(filename, 'rb')
    key = f.read()
    f.close()
    return key


def encrypt(message, key):
    message = _pad(message)
    IV = Random.new().read(AES.block_size)
    aes = AES.new(key, AES.MODE_CBC, IV)
    return base64.b64encode(IV + aes.encrypt(str.encode(message)))


def decrypt(encrypted, key):
    encrypted = base64.b64decode(encrypted)
    IV = encrypted[:AES.block_size]
    aes = AES.new(key, AES.MODE_CBC, IV)
    return _unpad(aes.decrypt(encrypted[AES.block_size:])).decode('utf-8')


def encrypt_file(filename, key):
    f = open(filename, 'r')
    text = f.read()
    f.close()
    enc = encrypt(text, key)
    f=open(filename,'wb')
    f.write(enc)
    f.close()


def decrypt_file(filename, key):
    f = open(filename, 'rb')
    enc = f.read()
    f.close()
    text = decrypt(enc, key)
    f = open(filename, 'w')
    f.write(text)
    f.close()


def _pad(s):
    return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)


def _unpad(s):
    return s[:-ord(s[len(s) - 1:])]


if __name__ == '__main__':
    key = get_key('.\\key\\aes.key')
    print('key: ', key)
    decrypt_file('.\\files\\input.txt',key)