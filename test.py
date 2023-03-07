import pandas
import requests
import os
import json

url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
cwd = os.getcwd()
key = 'CompactData/DOT/M..TXG_FOB_USD.W00.?startPeriod=2022'

req = requests.get(f'{url}{key}').json()
data = req['CompactData']['DataSet']['Series']

# json_obj = json.dumps(data, indent = 1)
# with open(os.path.join(cwd, "check.json"), "w") as outfile:
#     outfile.write(json_obj)

# with open('check.json', encoding='utf-8') as inputfile:
#     df = pandas.read_json(inputfile)
# df.to_csv(os.path.join(cwd, 'csvfile.csv'), encoding='utf-8', index=False)

list = []
for country in data:
    list.append(country['Obs'])
df = pandas.df(list)
df.to_csv(os.path.join(cwd, 'checkMeeee.csv'), header = True)
# df = pandas.DataFrame({country['@COUNTERPART_AREA'] : {pandas.to_datetime(stats['@TIME_PERIOD']) : 
#      round(float(stats['@OBS_VALUE']), 1) for stats in country["Obs"]} 
#      for country in data})

# param = [('dataset', 'DOT'),
#          ('freq', 'M'),
#          ('country', ''),
#          ('series', 'TXG_FOB_USD'),
#          ('partner', 'W00'),
#          ('start', '?startPeriod=2020')]

# series = '.'.join([i[1] for i in param[1:5]])
# key = f'CompactData/{param[0][1]}/{series}{param[-1][1]}'

# r = requests.get(f'{url}{key}').json()
# data = r['CompactData']['DataSet']['Series']

# json_obj = json.dumps(data, indent = 1)
# with open(os.getcwd() + "/check.json", "w") as outfile:
#     outfile.write(json_obj)

# df = pandas.DataFrame({s['@REF_AREA']: # Each country/area
#                    {i['@TIME_PERIOD']: float(i['@OBS_VALUE']) 
#                     for i in s['Obs']} for s in data})
# df.to_csv(os.path.join(cwd, "new_test.csv"), header = True)