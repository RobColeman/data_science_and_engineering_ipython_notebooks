# data_science_ipython_notebooks
A collection of examples ranging from algorithms, general programming, library use, machine learning, data mining, and data visualization.

This is not meant to be polished collection of works.  Notably absent are explinations for many applications, algorithms or problems.  Little, if any proof-reading has taken place, so read at your own risk.


## requirements:

There are a mix of Python 2.7 and Python 3 notebooks in here.  Support for the Python 3 required packages is still in progress.

The required python 2.7 packages can be installed with the following command

`pip install -r requirements.txt`

## installing spark

To download Spark go [here](http://spark.apache.org/downloads.html) and select the pre-built version you desire.  Then unpack it in the location of your choosing.

All done.

## Setting environment variables

Some of the examples require included datasets.  These are accessed using realative pathing by initializing some environment variables.

Additionally, there are some spark examples, which require you to download a prebuilt version of spark > 1.5.1.  The library will also require environment variables to be set to indicate the location of the spark library.

To set these environment variables, there is a script "setup.sh" which will set these.  Change the paths in this file to reflect the install location of this library and spark.  If you chose to not use spark, comment out the lines refering to spark.

Then run the following command:

`source setup.sh`


