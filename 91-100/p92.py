def next_num(n):
    """
    Return the integer k which
    is the sum of the squares of the
    digits of n.
    """
    n = map(lambda x: int(x) ** 2, str(n))
    return sum(n)


def square_digits(n):
    # whole_memory will record whether a number
    # hits 1 or 89 in the process defined

    # tmp_memory will be used to record the
    # numbers hit from a specific starting point
    # until we get to something in whole_memory

    whole_memory, tmp_memory = {1: {1}, 89: {89}}, set()
    for i in range(2, n+1):

        # once cur_num is in whole_memory[k] for some key k
        # we know where evey number in tmp_memory will
        # end up -- since they all end up
        # at  the value k. Use the list memory_check to keep
        # track of these final values. Once one is hit,
        # we can halt our process and fill the values we've
        # encountered

        cur_num = i
        memory_check = []
        while not memory_check:
            tmp_memory.add(cur_num)
            cur_num = next_num(cur_num)
            memory_check = [k for k, v in whole_memory.items() if cur_num in v]

        final, = memory_check
        whole_memory[final].update(tmp_memory)
        tmp_memory = set()

    return whole_memory


if __name__ == "__main__":
    t = square_digits(10_000_000)
    print([(k, len(v)) for k, v in t.items()])
