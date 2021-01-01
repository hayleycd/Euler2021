# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def largest_prime_factor(number_to_check):
    for potential_factor in range(1, number_to_check//2):
        if number_to_check % potential_factor == 0:
            factor_pair = number_to_check // potential_factor
            is_prime = is_prime(factor_pair)
            if is_prime:
                 return factor_pair

def is_prime(factor_to_check):
    # to do: write a function to determine if a number is prime. 
    return True