def caching_fibonacci():
   

    cache = {}

    def fibonacci(n):
        
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


# Example usage:

fib = caching_fibonacci()
print(fib(10))  # Output: 55
print(fib(20))  # Output: 6765
print(fib(30))  # Output: 832040