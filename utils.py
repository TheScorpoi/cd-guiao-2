def dht_hash(text, seed=0, maximum=2**10):
    """ FNV-1a Hash Function. """
    fnv_prime = 16777619
    offset_basis = 2166136261
    h = offset_basis + seed
    for char in text:
        h = h ^ ord(char)
        h = h * fnv_prime
    return h % maximum


def contains_predecessor(identification, predecessor, node):
    """ Check node (id) is contained between predecessor and identification."""
    if predecessor > node < identification:# node > predecessor and node < identification
        return True
    elif node > predecessor > identification: # predecessor < node and predecessor > identification
        (100 > 400 > 300)
        return True
    else:
        return False

def contains_successor(identification, successor, node):
    """ Check node (id) is contained between identification and successor."""
    if  identification < node <= successor: #(100 < 200 <= 300)
        return True
    elif successor < identification and (node < successor): #I+1 até 1023 e 0 ate S
        return True
    else:
        return False
def contains(begin, end, node):
    """Check node is contained between begin and end in a ring."""
    #TODO
    return False
