def ean13_to_dun14(ean13, units_number):
    units_number = int(units_number)

    if units_number >= 1 and units_number <= 6:
        first_digit = "1"
    elif units_number >= 7 and units_number <= 10:
        first_digit = "2"
    elif units_number >= 11 and units_number <= 12:
        first_digit = "3"
    elif units_number >= 13 and units_number <= 20:
        first_digit = "4"
    elif units_number >= 21 and units_number <= 24:
        first_digit = "5"
    else:
        raise ValueError("Invalid number of units")

    ean13_digits = [int(d) for d in ean13]
    odd_sum = sum(ean13_digits[0::2])
    even_sum = sum(ean13_digits[1::2]) * 3
    total_sum = odd_sum + even_sum
    check_digit = (10 - (total_sum % 10)) % 10
    dun14 = first_digit + ean13[:-1] + str(check_digit)
    return dun14
