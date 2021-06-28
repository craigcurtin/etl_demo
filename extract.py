

def extract_from_csv(file_to_process): 
    dataframe = pd.read_csv(file_to_process) 
    return dataframe

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process,lines=True)
    return dataframe

def extract_from_xml(file_to_process):

    dataframe = pd.DataFrame(columns=['car_model','year_of_manufacture','price', 'fuel'])
    tree = ET.parse(file_to_process) 
    root = tree.getroot() 

    for person in root: 
        car_model = person.find("car_model").text 
        year_of_manufacture = int(person.find("year_of_manufacture").text)
        price = float(person.find("price").text) 
        fuel = person.find("fuel").text 
        dataframe = dataframe.append({"car_model":car_model, "year_of_manufacture":year_of_manufacture, "price":price, "fuel":fuel}, ignore_index=True) 
        return dataframe


def extract():
	extracted_data = pd.DataFrame(columns=['car_model','year_of_manufacture','price', 'fuel']) 
    #for csv files
      for csvfile in glob.glob("dealership_data/*.csv"):
          extracted_data = extracted_data.append(extract_from_csv(csvfile), ignore_index=True)
    #for json files
      for jsonfile in glob.glob("dealership_data/*.json"):
          extracted_data = extracted_data.append(extract_from_json(jsonfile), ignore_index=True)
    #for xml files
      for xmlfile in glob.glob("dealership_data/*.xml"):
          extracted_data = extracted_data.append(extract_from_xml(xmlfile), ignore_index=True)
      return extracted_data
