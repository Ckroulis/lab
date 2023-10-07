def sieve(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.reverse()
    return tuple(unique_numbers)

numbers = [1, 2, 3, 4, 4, 5, 5, 6]
result = sieve(numbers)
print(result)