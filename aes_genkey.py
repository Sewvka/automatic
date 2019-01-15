from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP


def gen_aes_key(filename, length):
    key = get_random_bytes(length)
    f = open(filename,'wb')
    f.write(key);
    f.close()

if __name__ == '__main__':
    gen_aes_key('keys\\wKEYpr1.txt', 256)