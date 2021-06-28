
import pandas as pd
from collections import defaultdict


def transform(data):
    data['price'] = round(data.price, 2)
    return data

class Transform(object):
    def __init__ (self):
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
                    data[field] = round(data.price, 2)
                # round attribute to next hundreds digit
                if transformation == 'ceil hundred':
                    data[field] = round(data.price, 2)
                # ... well, do you get it? see the pattern ?
        return data