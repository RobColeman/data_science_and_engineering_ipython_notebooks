import numpy as np

def cosine_distance(A,B):
  if type(A) == list:
    A = np.array(A)
  if type(B) == list:
    B = np.array(B)

  num = A.dot(B)
  den = np.linalg.norm(A) * np.linalg.norm(B)

  if den == 0:
    return 0.0
  else:
    return num / den


def hamming_distance(A,B):
  return sum([a==b for a,b in zip(A,B)])


def jaccard_index(A,B):
  A = set(A)
  B = set(B)
  return float(len(A.intersection(B))) / float(len(A.union(B)))