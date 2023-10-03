def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def list_primes(number):
    return [i for i in range(2, number + 1) if is_prime(i)]

def nth_prime(number):
    count = 0
    num = 2
    while True:
        if is_prime(num):
            count += 1
        if count == number:
            return num
        num += 1

print(is_prime(7))  # 期待する出力: True
print(is_prime(8))  # 期待する出力: False
print(list_primes(20))  # 期待する出力: [2, 3, 5, 7, 11, 13, 17, 19]
print(nth_prime(4))  # 期待する出力: 7
