class JavaCode: @staticmethod
def getRandomString():
    SALTCHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    salt = java.lang.StringBuilder()
    rnd = java.util.Random()
    while salt.length() < 18: # length of the random string.
        index = int((rnd.nextFloat() * len(SALTCHARS)))
        salt.append(SALTCHARS[index])
        saltStr = salt.toString()
    return saltStr
@staticmethod
def main(args): print("please work")
if __name__ == "__main__": JavaCode.main([])