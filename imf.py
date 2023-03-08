import os
import datetime
import json
import my_input
import pandas
import requests
from flatten_json import flatten

root = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
directory = os.path.join(os.getcwd(), "data")
json_path = os.path.join(directory, "my.json")

# dictionary to store country names as keys and corresponding country codes as values
country_dict = {} 

# function to add key-value pairs to country_dict, where keys = country names & values = country codes
def make_country_dict():
    country_key = 'DataStructure/DOT'
    dl = requests.get(f'{root}{country_key}').json()\
        ['Structure']['KeyFamilies']['KeyFamily']['Components']['Dimension']
    country_key = f"CodeList/{dl[1]['@codelist']}"
    cl = requests.get(f'{root}{country_key}').json()['Structure']['CodeLists']['CodeList']['Code']
    for c in cl:
        key = c['Description']['#text']
        value = c['@value']
        country_dict[key] = value

# function to write countries and their corresponding codes to a csv file
def get_countries():
   df = pandas.DataFrame.from_dict(country_dict, orient = "index")
   file_path = os.path.join(directory, "imf_country_codes.csv")
   df.to_csv(file_path)

# function to write export data to a csv file for a country pair, starting at year designated by start
def get_pair_exports():
   def pair(rep, part, start, freq):
      if (freq == "B"):
         pair(rep, part, start, "A")
         pair(rep, part, start, "M")
      else:
         reporter = country_dict[rep]
         partner = country_dict[part]
         file_name = f'imf_{reporter}_to_{partner}_exports_{start}{freq}.csv'
         year = int(datetime.date.today().year) - 3
         if int(start) > year:
            if freq == 'A':
               start = str(year)
         file_path = os.path.join(directory, file_name)
         param = [('dataset', 'DOT'),
            ('freq', freq),
            ('country', reporter),
            ('series', 'TXG_FOB_USD'),
            ('partner', partner),
            ('start', f'?startPeriod={start}')]
         series = '.'.join([i[1] for i in param[1:5]])
         key = f'CompactData/{param[0][1]}/{series}{param[-1][1]}'
         data = requests.get(f'{root}{key}').json()['CompactData']['DataSet']['Series']
         data_list = [[obs.get('@TIME_PERIOD'), obs.get('@OBS_VALUE')]
            for obs in data['Obs']]
         df = pandas.DataFrame(data_list, columns = ["Date", "Value (Millions USD)"])
         df["Reporter"] = param[2][1]
         df["Partner"] = param[4][1]
         df.to_csv(file_path)
   make_country_dict()
   specs = ["country", "country", "year", "freq"]
   input_list = my_input.get_input(specs, country_dict)
   pair(input_list[0], input_list[1], input_list[2], input_list[3])
   print("All done! Check the data folder to see your new files.\n")

# function to get each country's total exports for a given year (returns data for specified year only)
def get_total_exports():
   def total(freq, year):
      if freq == "B":
         total("A", year)
         total("M", year)
      else:
         csv_path = os.path.join(directory, f'imf_total_exports_{year}{freq}.csv')
         key = f'CompactData/DOT/{freq}..TXG_FOB_USD.W00.?startPeriod={year}'
         req = requests.get(f'{root}{key}').json()
         data = req['CompactData']['DataSet']['Series']
         json_obj = json.dumps(data, indent = 1)
         with open(json_path, "w") as output_file:
            output_file.write(json_obj)
         with open(json_path, "r") as input_file:
            data = json.load(input_file)
         df = pandas.DataFrame([flatten(country) for country in data])
         df.to_csv(csv_path)
         os.remove(json_path)
   specs = ["freq", "year"]
   input_list = my_input.get_input(specs, None)
   total(input_list[0], input_list[1])
   print("All done! Check the data folder to see your new files.\n")

# putting it all together
def main():
   get_total_exports()
   get_pair_exports()
   get_countries()

if __name__ == "__main__":
    main()





