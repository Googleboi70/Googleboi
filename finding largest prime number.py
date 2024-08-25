largest_prime= None
for num in range(25, 51):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            if largest_prime is None or num > largest_prime:
                largest_prime = num

if largest_prime is not None:
    print("Largest prime number:", largest_prime)
else:
    print("No prime numbers found in this range.")