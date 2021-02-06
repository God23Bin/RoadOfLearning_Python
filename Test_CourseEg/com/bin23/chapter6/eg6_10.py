def printChars(ch1,ch2,number):
    count = 0
    for i in range(ord(ch1), ord(ch2) + 1):
        count += 1
        if count % number != 0:
            print("%4s" % chr(i), end="")
        else:
            print("%4s" % chr(i))

printChars("!", "9",10)