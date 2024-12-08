def get_multiplied_digits(number):

    str_number = str(number)

    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number)

result_1 = get_multiplied_digits(40203)
print(result)

result_2 = get_multiplied_digits(402030)
print(result)













