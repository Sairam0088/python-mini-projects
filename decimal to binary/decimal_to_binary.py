# decimal to binary

def decimal_to_binary(decimal):
    binary = ""
    
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    return binary


decimal = int(input("Enter a decimal: "))
binary = decimal_to_binary(decimal)

print("Binary Representation:",binary)