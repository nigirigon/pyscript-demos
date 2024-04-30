from pyscript import display
m="Ready to play !"
display(m, target="main_pyscript")

import modin.pandas as pd
import pandas

#############################################
### For the purpose of timing comparisons ###
#############################################
import time
import ray
# Look at the Ray documentation with respect to the Ray configuration suited to you most.
ray.init()
#############################################

# This may take a few minutes to download
import urllib.request
dataset_url = "https://modin-datasets.intel.com/testing/yellow_tripdata_2015-01.csv"
urllib.request.urlretrieve(dataset_url, "taxi.csv")

start = time.time()

pandas_df = pandas.read_csv(dataset_url, parse_dates=["tpep_pickup_datetime", "tpep_dropoff_datetime"], quoting=3)

end = time.time()
pandas_duration = end - start
print("Time to read with pandas: {} seconds".format(round(pandas_duration, 3)))


#
start = time.time()

modin_df = pd.read_csv(dataset_url, parse_dates=["tpep_pickup_datetime", "tpep_dropoff_datetime"], quoting=3)

end = time.time()
modin_duration = end - start
print("Time to read with Modin: {} seconds".format(round(modin_duration, 3)))

print("Modin is {}x faster than pandas at `read_csv`!".format(round(pandas_duration / modin_duration, 2)))