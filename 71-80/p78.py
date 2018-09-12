import time


class PartitionNumbers:
    def __init__(self):
        self.partition_numbers = [1, ]

    def get_next(self):
        def peng_index_gen():
            """
            An infinite generator for the ms in the
            generalized pentagonal numbers.
            """
            yield 0
            m = 1
            while True:
                yield m
                if m > 0:
                    m *= -1
                else:
                    m = -m + 1

        def pent_num_gen():
            """
            An infinite generator for generalized pentagonal numbers
            """
            m_gen = peng_index_gen()
            while True:
                m = next(m_gen)
                yield m * (3 * m - 1)//2

        def prev_index_gen():
            """
            For an integer n, yields the indexes of
            partition numbers used in the pentagonal number
            recursive formula for partition numbers
            """
            pent_nums = pent_num_gen()

            cur_pent_num = next(pent_nums)
            cur_pent_num = next(pent_nums)

            while n - cur_pent_num >= 0:
                yield n - cur_pent_num
                cur_pent_num = next(pent_nums)

        n = len(self.partition_numbers)
        prev_indexes = prev_index_gen()

        new_part_number = sum(
            (-1)**(k % 4 in {2, 3}) * self.partition_numbers[x]
            for k, x in enumerate(prev_indexes)
            )
        self.partition_numbers.append(new_part_number)


if __name__ == "__main__":

    modulus = 1_000_000
    start_time = time.time()

    c = PartitionNumbers()
    cur_par_num = c.partition_numbers[-1]

    while cur_par_num % modulus != 0:
        c.get_next()
        cur_par_num = c.partition_numbers[-1]

    print(time.time() - start_time)
    print(len(c.partition_numbers) - 1)
