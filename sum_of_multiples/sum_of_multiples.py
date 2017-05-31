def sum_of_multiples(limit, multiples=None):
    if not multiples:
        return 0
    if multiples[0] == 0:
        # multiples of 0 don't change the sum
        multiples = multiples[1:]
    return sum(value for value in range(limit)
               if any(value % multiple == 0
                      for multiple in multiples))
