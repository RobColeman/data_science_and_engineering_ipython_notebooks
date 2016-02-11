import numpy as np

def cosine_distance(A,B):
    if type(A) == list:
        A = np.array(A)
    if type(B) == list:
        B = np.array(B)

    num = A.dot(B)
    denom = np.linalg.norm(A) * np.linalg.norm(B)

    if denom == 0:
        return 0.0
    else:
        return num / denom


def hamming_distance(A,B):
    return sum([a==b for a,b in zip(A,B)])


def jaccard_index(A,B):
    A = set(A)
    B = set(B)
    return float(len(A.intersection(B))) / float(len(A.union(B)))


def jaccard_distance(A,B):
    return 1.0 - jaccard_index(A,B)

def tanimoto_distance(A,B):
    """
    for bit vector representation of sets
    """
    if type(A) == list:
        A = np.array(A)
    if type(B) == list:
        B = np.array(B)

    num = float(A.dot(B))
    denom = float(A.sum()**2 + B.sum()**2 - num)

    if denom == 0:
        return 0.0
    else:
        return num / denom


def cross_entropy_multinomial(true, test):
    if not len(true) == len(test):
        raise Exception('distributions must be of the same length')
    total = 0
    for p,q in zip(true,test)
        total -= p * np.log(q)
    return total


def kl_distance(p, q):
    p = np.asarray(p, dtype=np.float)
    q = np.asarray(q, dtype=np.float)
    return np.sum(np.where(p != 0,(p-q) * np.log10(p / q), 0))
