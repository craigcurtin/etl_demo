

def transform(data):
       data['price'] = round(data.price, 2)
       return data


