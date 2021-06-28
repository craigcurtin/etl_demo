import pandas as pd
import glob
import xml.etree.ElementTree as ET


class Extract(object):
    def __init__(self, source_directory):
        self.target_directory = source_directory

    def run(self):
        extracted_data = pd.DataFrame(columns=['car_model', 'year_of_manufacture', 'price', 'fuel'])
        # for csv files
        for csvfile in glob.glob("{}/*.csv".format(self.target_directory)):
            extracted_data = extracted_data.append(self.extract_from_csv(csvfile), ignore_index=True)
            # for json files
        for jsonfile in glob.glob("{}/*.json".format(self.target_directory)):
            extracted_data = extracted_data.append(self.extract_from_json(jsonfile), ignore_index=True)
            # for xml files
        for xmlfile in glob.glob("{}/*.xml".format(self.target_directory)):
            extracted_data = extracted_data.append(self.extract_from_xml(xmlfile), ignore_index=True)

        return extracted_data

    def extract_from_csv(self, file_to_process):
        dataframe = pd.read_csv(file_to_process)
        return dataframe

    def extract_from_json(self, file_to_process):
        dataframe = pd.read_json(file_to_process, lines=True)
        return dataframe

    def extract_from_xml(self, file_to_process):
        dataframe = pd.DataFrame(columns=['car_model', 'year_of_manufacture', 'price', 'fuel'])
        tree = ET.parse(file_to_process)
        root = tree.getroot()
        for person in root:
            car_model = person.find("car_model").text
            year_of_manufacture = int(person.find("year_of_manufacture").text)
            price = float(person.find("price").text)
            fuel = person.find("fuel").text
            dataframe = dataframe.append(
                {"car_model": car_model, "year_of_manufacture": year_of_manufacture, "price": price, "fuel": fuel},
                ignore_index=True)
            return dataframe
