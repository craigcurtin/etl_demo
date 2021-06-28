import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime
import logging

from extract import Extract
from transform import Transform
from load import Load

tmpfile = "dealership_temp.tmp"  # store all extracted data
logfile = "dealership_logfile.txt"  # all event logs will be stored
target = "dealership_transformed_data.csv"  # transformed data is stored

if __name__ == '__main__':
    logging.info("ETL Job Started")

    logging.info("Extract, all from [CSV && XML && JSON], Started")
    Extract = Extract('Data')
    extract_data = Extract.run()
    logging.info("Extract, complete")

    Transform = Transform()
    Transform.transformation('price', 'two_digits')
    Transform.transformation('price', 'ceil hundred')
    transform_data = Transform.apply(extract_data)
    logging.info("Transform, complete")

    logging.info("Load phase Started")
    Load = Load()
    Load.persist(target, transform_data)
    logging.info("Load, complete")

    logging.info("ETL, complete")
