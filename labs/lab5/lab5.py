#1
def time_converter(value, from_unit, to_unit):
    units_to_seconds = {
        'sec': 1,
        'min': 60,
        'hour': 3600,
        'day': 86400
    }
    if from_unit not in units_to_seconds or to_unit not in units_to_seconds:
        return "Ошибка: неверная единица времени"

    value_in_seconds = value * units_to_seconds[from_unit]
    result = value_in_seconds / units_to_seconds[to_unit]

    return round(result, 2)

print(time_converter(4, 'hour', 'min'))
print(time_converter(30, 'min', 'hour'))
print(time_converter(12, 'sec', 'min'))

#2
def calculate_deposit(amount, years):

    if amount < 30000:
        return "Ошибка: Минимальный депозит - 30000"

    rate = min(0.3 * (amount // 10000) / 100, 0.05)

    if years <= 3:
        rate += 0.03
    elif years <= 6:
        rate += 0.05
    else:
        rate += 0.02

    total_amount = amount * ((1 + rate) ** years)

    profit = total_amount - amount
    return round(profit, 2)

print(calculate_deposit(30000, 3))
print(calculate_deposit(100000, 5))
print(calculate_deposit(200000, 8))

#3
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes(start, end):
    if start < 0 or end < 0 or start > end:
        print("Error!")
        return
    primes = [str(num) for num in range(start, end + 1) if is_prime(num)]
    if primes:
        print(" ".join(primes))
    else:
        print("Error!")
print("Введите два числа через пробел:")
start, end = map(int, input().split())
print_primes(start, end)

#4
print('введите размер матрицы')
n = int(input())

if n > 2:
    print('error')
else:
    print('введите первую матрицу')
    matrix1 = []
    for i in range(n):
        l = list(map(float, input().split()))
        matrix1.append(l)

    print('введите вторую матрицу')
    matrix2 = []
    for i in range(n):
        l = list(map(float, input().split()))
        matrix2.append(l)

    result = []
    for i in range(n):
        new_r = []
        for j in range(n):
            new_r.append(matrix1[i][j] + matrix2[i][j])
        result.append(new_r)
    print('результат:')

    for l in result:
        print(' '.join(str(x) for x in l))


#5
def is_palindrome(text):

    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())

    return cleaned_text == cleaned_text[::-1]

print(is_palindrome("всем привет подпишитесь на канал"))
print(is_palindrome("лёша на полке клопа нашёл"))

print(is_palindrome("алфавитный порядок"))
