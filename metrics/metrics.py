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