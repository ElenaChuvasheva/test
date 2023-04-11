n = 40

def numbers(n):
    a = 1
    counter = 0
    symbols = []
    for _ in range(n):
        symbols.append(str(a))
        counter += 1
        if counter == a:
            a += 1
            counter = 0
    print(''.join(symbols))

if __name__ == '__main__':
    print('Введите натуральное число:')
    n = int(input())
    numbers(n)