# trigger_review.py

import math
import time

def compute_primes(n):
    # Inefficient: checks every number up to n for primality
    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

def slow_factorial(x):
    # Recursive without memoization → will blow the stack
    if x <= 1:
        return 1
    return x * slow_factorial(x - 1)

def main():
    # No input validation, bare exceptions, sleeps unnecessarily
    try:
        num = int(input("Enter a number: "))
    except:
        print("Invalid!")
    time.sleep(2)
    primes = compute_primes(num)
    fact = slow_factorial(num)
    print(f"Primes < {num}: {primes}")
    print(f"{num}! = {fact}")

if __name__ == "__main__":
    main()
