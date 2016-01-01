import os
import sys


def load_delimited(path,delimiter = ","):
    f = open(path,"r+")
    return [l.replace("\n","").split(delimiter) for l in f if not l == "\n"]