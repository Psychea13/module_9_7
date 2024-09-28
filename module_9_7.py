def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        if res == 0 or res == 1:
            print('Не простое и не составное число:')
        elif res < 0:
            print('Отрицательное число нельзя проверить')
        else:
            for i in range(2, int(res ** 0.5 + 1)):
                if res % i == 0:
                    print('Составное число:')
                    break
            else:
                print('Простое число:')
        return res
    return wrapper


@is_prime
def sum_three(*args: int):
    return sum(args)


print('Приветствую! Это проверка на простые и составные числа.')

result = sum_three(2, 3, 6)
print(result)

result = sum_three(5, 1, 0)
print(result)

result = sum_three(0, 0, 0)
print(result)

result = sum_three(0, 0, 1)
print(result)

result = sum_three(0, 0, -1)
print(result)
