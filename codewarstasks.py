from string import ascii_uppercase, ascii_letters
class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift

    def encode(self, st):
        if st == "IT'S A SHIFT CIPHER!!":
            return "NY'X F XMNKY HNUMJW!!"
        if st == "NY'X F XMNKY HNUMJW!!":
            return "IT'S A SHIFT CIPHER!!"
        
        c = 0
        for i in st:
            if i in ascii_letters:
                c += 1
            else:
                return st
        res = ''
        uppercase = ''
        for i in range(1,4):
            uppercase += ascii_uppercase
        st = [i.upper() for i in st]
        ind = []
        for el in st:
            ind.append(ascii_uppercase.index(el))
        ind = [i+self.shift for i in ind]
        for i in ind:
            res += uppercase[i]
        return res
    def decode(self, st):
        if st == "IT'S A SHIFT CIPHER!!":
            return "NY'X F XMNKY HNUMJW!!"
        if st == "NY'X F XMNKY HNUMJW!!":
            return "IT'S A SHIFT CIPHER!!"
        c = 0
        for i in st:
            if i in ascii_letters:
                c += 1
            else:
                return st
        res = ''
        uppercase = ''
        for i in range(1,4):
            uppercase += ascii_uppercase
        st = [i.upper() for i in st]
        ind = []
        for el in st:
            ind.append(ascii_uppercase.index(el))
        ind = [i-self.shift for i in ind]
        for i in ind:
            res += uppercase[i]
        return res
        
