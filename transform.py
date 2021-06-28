import pandas as pd
import math
from collections import defaultdict


class Transform(object):
    """ Transform data in underlying Pandas DF, configure as many transformations as desired
        the transformations will be applied sequentially (list order, first in, first executed)
    """
    def __init__(self):
        self.transformations = defaultdict(list)

    def transformation(self, field, transform):
        self.transformations[field].append(transform)

    def apply(self, data):
        for field in self.transformations.keys():
            transformations = self.transformations[field]
            for transformation in transformations:
                # round attribute to two digits of precision
                if transformation == 'two_digits':
                    data[field] = round(data.price, 2)
                # round attribute to next tens digit
                if transformation == 'ceil ten':
                   # data[field] = float(math.ceil(data.price / 10.0)) * 10
                   data[field] = round(data.price, 4)
                # round attribute to next hundreds digit
                if transformation == 'ceil hundred':
                   # data[field] = float(math.ceil(data.price.astype(float) / 100.0) * 100)
                   data[field] = round(data.price, 3)
                # ... well, do you get it? see the pattern ?
        return data
