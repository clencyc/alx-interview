#!/usr/bin/python3

def isWinner(x, nums):
    if x <= 0 or not nums:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if play_game(n, primes):
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(max_num + 1) if is_prime[p]]

def play_game(n, primes):
    numbers = set(range(1, n + 1))
    turn = 0  # 0 for Maria, 1 for Ben
    
    while True:
        move_made = False
        for prime in primes:
            if prime in numbers:
                move_made = True
                multiples = set(range(prime, n + 1, prime))
                numbers -= multiples
                break
        if not move_made:
            return turn == 1
        turn = 1 - turn