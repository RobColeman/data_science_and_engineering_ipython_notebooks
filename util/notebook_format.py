# -*- coding: utf-8 -*-

"""Copyright 2015 Roger R Labbe Jr.


Code supporting the book

Kalman and Bayesian Filters in Python
https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python


This is licensed under an MIT license. See the LICENSE.txt file
for more information.
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from contextlib import contextmanager
from distutils.version import LooseVersion
from IPython.core.display import HTML
import json
import matplotlib
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import numpy as np
import os.path
import sys


sys.path.insert(0, './code') # allow us to import book_format

def test_filterpy_version():
    import filterpy
    min_version = [0,0,28]
    v = filterpy.__version__
    tokens = v.split('.')
    for i,v in enumerate(tokens):
        if int(v) > min_version[i]:
            return

    i = len(tokens) - 1
    if min_version[i] > int(tokens[i]):
       raise Exception("Minimum FilterPy version supported is {}.{}.{}.\n"
                       "Please install a more recent version.\n"
                       "   ex: pip install filterpy --upgrade".format(
             *min_version))
    v = int(tokens[0]*1000)


# ensure that we have the correct filterpy loaded. This is
# called when this module is imported at the top of each book
# chapter so the reader can see that they need to update FilterPy.
test_filterpy_version()


def equal_axis():
    pylab.rcParams['figure.figsize'] = 10,10
    plt.axis('equal')


def reset_axis():
    pylab.rcParams['figure.figsize'] = 11, 4

def set_figsize(x=11, y=4):
    pylab.rcParams['figure.figsize'] = x, y


@contextmanager
def figsize(x=11, y=4):
    """Temporarily set the figure size using 'with figsize(a,b):'"""

    size = pylab.rcParams['figure.figsize']
    set_figsize(x, y)
    yield
    pylab.rcParams['figure.figsize'] = size

@contextmanager
def numpy_precision(precision):
  old = np.get_printoptions()['precision']
  np.set_printoptions(precision=precision)
  yield
  np.set_printoptions(old)

@contextmanager
def printoptions(*args, **kwargs):
    original = np.get_printoptions()
    np.set_printoptions(*args, **kwargs)
    yield
    np.set_printoptions(**original)

def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv

def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        rv[key] = value
    return rv


def load_style(directory = '.', name='code/custom.css'):
    if sys.version_info[0] >= 3:
        style = json.load(open(os.path.join(directory, "code/538.json")))
    else:
        style = json.load(open(directory + "/code/538.json"), object_hook=_decode_dict)

    # matplotlib has deprecated the use of axes.color_cycle as of version

    version = [int(version_no) for version_no in matplotlib.__version__.split('.')]
    if version[0] > 1 or (version[0] == 1 and version[1] >= 5):
        style["axes.prop_cycle"] = "cycler('color', ['#6d904f','#013afe', '#202020','#fc4f30','#e5ae38','#A60628','#30a2da','#008080','#7A68A6','#CF4457','#188487','#E24A33'])"
        style.pop("axes.color_cycle", None)

    plt.rcParams.update(style)
    reset_axis ()
    np.set_printoptions(suppress=True)

    styles = open(os.path.join(directory, name), 'r').read()
    return HTML(styles)

