import operator

def distance(dna1, dna2):
    if len(dna1)==len(dna2):
        return map(operator.eq, dna1, dna2).count(False)
    else:
        raise ValueError
