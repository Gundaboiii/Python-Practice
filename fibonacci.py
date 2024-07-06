def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Input number of terms from the user
n = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Calling the fibonacci function
fibonacci_sequence = fibonacci(n)

# Printing the Fibonacci sequence
print("Fibonacci sequence:", fibonacci_sequence)
