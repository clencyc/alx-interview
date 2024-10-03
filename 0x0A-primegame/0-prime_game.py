#!/usr/bin/python3

"""
Sieve of Eratosthenes
"""


def isWinner(x, nums):
    """
    Primagame function
    That determines the winner of the game
    """
    def sieve(n):
        """ Use Sieve of Eratosthenes
        to find all primes up to n """

        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] is True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        is_prime[0], is_prime[1] = False, False
        return [p for p in range(n + 1) if is_prime[p]]

    def game_winner(n):
        """
        Determines the winner
        """

        if n == 1:
            return "Ben"

        primes = sieve(n)
        moves = 0
        current_set = set(range(1, n + 1))

        for prime in primes:
            if prime in current_set:
                moves += 1
                multiples = set(range(prime, n + 1, prime))
                current_set -= multiples

        return "Maria" if moves % 2 != 0 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        winner = game_winner(num)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None