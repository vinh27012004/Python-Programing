def fibonacci_max(a):
    if a < 1:
        return None

    fib1, fib2 = 1, 1
    while fib2 <= a:
        fib1, fib2 = fib2, fib1 + fib2

    return fib1

# Input
a = int(input("Nhập vào số nguyên dương a: "))

# Output
result = fibonacci_max(a)
print(f"Số lớn nhất trong dãy số Fibonacci và không lớn hơn {a} là: {result}")