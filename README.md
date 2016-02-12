# data_science_ipython_notebooks
a collection of examples ranging from algorithms, general programming, library use, machine learning, data mining, and data visualization


## requirements:

The reuqired python packages can be installed with the following command

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


