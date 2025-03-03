# Trả về danh sách nguyên tố của n
def get_prime(n):
    prime = []
    for i in range(2, n + 1):
        while n % i == 0:
            prime.append(i)
            n //= i
    return prime

def create_prime_factor(numbers):
    prime_factors = {}
    for number in numbers:
        prime_factors[number] = get_prime(number)
    return prime_factors

# Nhập số nguyên dương
numbers = list(map(int, input("Nhập số nguyên dương: ").split()))
prime_factors = create_prime_factor(numbers)
print(prime_factors)