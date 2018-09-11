import sympy
import time
from collections import defaultdict


class PrimePartitions:

    def __init__(self, n=None):
        self.sieve = sympy.sieve
        self.partitions = defaultdict(set)
        self.partitions[2] = {(2,)}

    def get_next_layer(self):
        """
        updates the dictionary of prime partitions to the next number.
        """
        n = max(self.partitions)
        num = n + 1
        if num in self.sieve.primerange(2, num+1):
            self.partitions[num].update({(num,)})
        num_primes = [p for p in range(2, num+1) if p in self.sieve.primerange(2, num+1)]

        for prime in num_primes:
            num_partitions_prime = {
                tuple(sorted((prime, *old_partition)))
                for old_partition in self.partitions[num - prime]
            }
            self.partitions[num].update(num_partitions_prime)


def wrapper(upper=1_000):
    prime_sums = PrimePartitions()
    m_sums = 1
    counter = 2

    while m_sums <= upper:
        prime_sums.get_next_layer()
        counter += 1
        m_sums = max(
            len(prime_sums.partitions[counter]),
            m_sums
        )
    return counter


if __name__ == "__main__":
    start_time = time.time()
    print(wrapper(5_000))
    print(time.time() - start_time)
