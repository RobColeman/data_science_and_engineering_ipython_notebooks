import numpy as np
from sklearn.datasets import make_blobs


# center and sphere data
def center_and_sphere(data_RDD):
    # we can do these stasts steaming in O(n)
    n = float(data_RDD.count())
    arrays = data_RDD.map( lambda t: t[1] )
    mean = arrays.reduce( lambda a, b: a + b ) / n
    vi = lambda x: (x - mean)**2
    std = np.sqrt(arrays.map( vi ).reduce(lambda a, b: a + b) / n)
    normalize = lambda t: (t[0], (t[1] - mean) / std )
    return data_RDD.map(normalize)





def make_blobs_rdd(N,d,k,sigma,bound,sc):
    X, y = make_blobs(n_samples=N, 
           n_features=d,
           centers=k, 
           cluster_std=sigma, 
           center_box=(-bound, bound), 
           shuffle=True)
    data = [(int(y[idx]), row) for idx, row in enumerate(X)]
    return center_and_sphere(sc.parallelize(data))