class Math:

    def __alphabet2int__(self, char):
        return {
            "0" : 0,
            "1" : 1,
            "2" : 2,
            "3" : 3,
            "4" : 4,
            "5" : 5,
            "6" : 6,
            "7" : 7,
            "8" : 8,
            "9" : 9,
            "A" : 10,
            "B" : 11,
            "C" : 12,
            "D" : 13,
            "E" : 14,
            "F" : 15,
            "G" : 16,
            "H" : 17,
            "I" : 18,
            "J" : 19,
            "K" : 20,
            "L" : 21,
            "M" : 22,
            "N" : 23,
            "O" : 24,
            "P" : 25,
            "Q" : 26,
            "R" : 27,
            "S" : 28,
            "T" : 29,
            "U" : 30,
            "V" : 31,
            "W" : 32,
            "X" : 33,
            "Y" : 34,
            "Z" : 35,
        }[char]

    def __alphabet2int__(self, char):
        return {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'}[char]        

    def b2dec(self, num_str, b):
        inv_num_str = num_str[::-1]
        result = 0
        for i in range(len(num_str)):
            result += self.__alphabet2int__(inv_num_str[i])*(b**i)
        return result

    def dec2b(self, num_str, b):
        result = str()
        while True:
            remain = num_str % b
            result += self.__alphabet2int__(remain)
            num_str = num_str // b
            if num_str == 1:
                result += self.__alphabet2int__(num_str)
                break
            elif num_str == 0:
                break
        return result[::-1]

    def get_divisor(self, num):
        result = list()
        for n in range(1, num+1):
            if num % n ==0:
                result.append(n)
        return result
    
    def get_gcd(self, a, b):
        if a>=b:
            ds = a
            db = b
        else:
            ds = b
            db = a
        quot = ds % db
        if quot == 0:
            return db
        else:
            return self.get_gcd(db, quot)
        
    def get_lcm(self, a, b):
        gcd = self.get_gcd(a, b)
        return a*b // gcd