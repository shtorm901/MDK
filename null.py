def search(number):
    number = int(number)
    num = 0
    value = abs(number)

    while value != 0:
        num += int(value % 10 == 0)
        value //= 10

    return(num)


print(search(100020))