# roman numerals to decimals using python

def roman_to_decimal(roman):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    prev_value = 0
    for i in reversed(roman):
        value = roman_numerals[i]
        if value < prev_value:
            decimal -= value
        else:
            decimal += value
        prev_value = value
    return decimal

roman = input("Enter a roman numeral: ").upper()
print("Decimal Equivalent:",roman_to_decimal(roman))
