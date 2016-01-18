import os
import sys


def load_delimited(path,delimiter = ","):
    f = open(path,"r+")
    return [l.replace("\n","").split(delimiter) for l in f if not l == "\n"]

def get_english_dictionary():
    p = os.environ.get('DATA_HOME', None) + "/text/words/en"
    f = open(p,"r+")
    return [w.replace("\n","") for w in f.readlines() if not w == "\n"]

