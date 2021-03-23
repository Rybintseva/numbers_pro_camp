with open('number.txt', 'r') as numbers:
    numbers_sum = 0
    for line in numbers.readlines():
        if not line.startswith('#') and line.strip() != '':
            numbers_sum = numbers_sum + float(line.strip())
    print(numbers_sum)
