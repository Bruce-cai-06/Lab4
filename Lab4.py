#fibonacci

def fibonacci(integer):
    a1 = 0
    b2 = 1
    c3 = 1
    if integer == 1:
        return 0
    if integer == 2:
        return 1
    if integer == 3:
        return 1
    for i in range(3, integer):
        a1 = b2
        b2 = c3
        c3 = a1 + b2
    return c3

# prime numbers

def is_prime(num):
    prime = 2
    if num == 1 or num == 0:
        return "False"
    for i in range(1,9):
        if num % prime == 0 and num != prime:
            return "False"
        else:
            prime += 1
            while prime % 2 == 0 or prime % 3 == 0 or prime % 5 == 0 or prime % 7 == 0 or prime % 11 == 0 or prime % 13 == 0 or prime % 17 == 0 or prime % 19 == 0:
                if prime == 2 or prime == 3 or prime == 5 or prime == 7 or prime == 11 or prime == 13 or prime == 17 or prime == 19 :
                    break
                prime += 1
    return "True"

'''            
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 11 == 0:
        if num == 2 or num == 3 or num == 5 or num == 7 or num == 11:
            return "True"
        else:
            return "False"
    elif num == 1 or num == 0:
        return "False"
    else:
        return "True"
'''

# Prime Factorization

def print_prime_factors(factor):
    if is_prime(factor):
        prime = 2
        count = 1
        while factor > 1:
            if factor % prime == 0:
                if count == 1:
                    print(f"{factor} = {prime}", end="")
                    factor = factor / prime
                    count += 1
                else:
                    factor = factor / prime
                    print(f" * {prime}", end="")
                    count += 1
            if factor == 1:
                break
            if factor % prime == 0:
                continue
            prime += 1
            if factor % prime != 0 and factor != 1:
                while prime % 2 == 0 or prime % 3 == 0 or prime % 5 == 0 or prime % 7 == 0 or prime % 11 == 0 or prime % 13 == 0 or prime % 17 == 0 or prime % 19 == 0:
                    if prime == 2 or prime == 3 or prime == 5 or prime == 7 or prime == 11 or prime == 13 or prime == 17 or prime == 19 :
                        break
                    else:
                        prime += 1
                        continue
            continue
        print("")
    else:
        print(factor)

print_prime_factors(25)