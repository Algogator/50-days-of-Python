def dec2bin(binary):
    bin = ""
    while binary != 0:
        bin = str(binary % 2) + bin
        binary = binary/2
    return bin


def bin2dec(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal


binary = input('enter a decimal no: ')
print dec2bin(binary)
binary = raw_input('enter a binary no: ')
print bin2dec(binary)
