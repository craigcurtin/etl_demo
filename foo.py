

import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime


tmpfile    = "dealership_temp.tmp"               # store all extracted data
logfile    = "dealership_logfile.txt"            # all event logs will be stored
targetfile = "dealership_transformed_data.csv"   # transformed data is stored

