# analyze results
def to_dict(tup):
    bucket, c = tup
    return (bucket, {c: 1})

def reduce_count_clusters(a,b):
    for k, v in a.items():
        if k in b:
            b[k] += v
        else:
            b[k] = v
    return b

def gini_impurity(tup):
    bucket, d = tup
    count = float(sum(d.values()))
    gini = 1 - sum([(float(v) / count)**2 for v in d.values()])
    return (bucket, gini, count)

def weighted_gini(A):
    buckets, ginis, counts = zip(*A)
    N = float(sum(counts))
    return sum([g*(c/N) for g,c in zip(ginis,counts)])

def to_bucket(vec):
    s = ""
    for j in vec:
        if j < 0: 
            s += str(0)
        elif j > 0:
            s += str(1)
        else:
            s += str(0)
    return int(s, 2)