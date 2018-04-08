import random
import seed
import calendar
import time

class Cipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, data):
        if len(data) > len(self.key):
            raise Exception("Cannot encrypt, block size must be less that seed!")
        data = [ord(x) ^ ord(y) for (x, y) in zip(data, self.key)]
        return bytes(data)

    def decrypt(self, data):
        if len(data) > len(self.key):
            raise Exception("Cannot decrypt, block size must be less that seed!")
        data = [ord(x) ^ ord(y) for (x, y) in zip(data, self.key)]
        return bytes(data)



if __name__ == "__main__":
    s = calendar.timegm(time.gmtime())
    random.seed(s)
    r = random.randint(1, s)
    c = Cipher(str(r)*len(seed.secret_message))
    ciphertext = c.encrypt(seed.secret_message)
    print(ciphertext)
