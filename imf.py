import requests
import os
import pandas
import json

#root url
url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
cwd = os.getcwd()

# #part of url that accesses exports from country to partner beginning at start date (yr)
# param = [('dataset', 'DOT'),
#          ('freq', 'M'),
#          ('country', 'IT'),
#          ('series', 'TXG_FOB_USD'),
#          ('partner', 'FR'),
#          ('start', '?startPeriod=2022')]
# series = '.'.join([i[1] for i in param[1:5]])

# #form rest of url after root
# key = f'CompactData/{param[0][1]}/{series}{param[-1][1]}'
# key = f'CompactData/DOT/M..TXG_FOB_USD.W00.?startPeriod=2022'

# # combine API url with key specific to data request
# r = requests.get(f'{url}{key}').json()

# # json_obj = json.dumps(r, indent=1)
# # with open(os.getcwd() + "/my_file.json", "w") as outfile:
# #     outfile.write(json_obj)

# data = r['CompactData']['DataSet']['Series']
# cwd = os.getcwd()
# data_list = {country['@REF_AREA']:{info['@TIME_PERIOD']: float(info['@OBS_VALUE']) for info in country['Obs']} for country in data}
# df = pandas.DataFrame(data_list)
# df.to_csv(os.path.join(cwd, "test.csv"), header = True)

# #create pandas data frame from the observations
# data_list = [[obs.get('@TIME_PERIOD'), obs.get('@OBS_VALUE')]
#     for obs in data['Obs']]
# df = pandas.DataFrame(data_list, columns = ["Date", "Value (Millions USD)"])

# #adding country + partner columns to data frame
# df["Country"] = param[2][1]
# df["Partner"] = param[4][1]

# #save cleaned dataframe as a csv file and save to data folder
# df.to_csv('export_ex.csv', header = True)
# cwd = os.getcwd() + "/data"
# df.to_csv(os.path.join(cwd, "tryme.csv"), header = True)

#second data set
param = [('dataset', 'DOT'),
        ('freq', 'M'),
        ('country', 'IT'),
        ('series', 'TXG_FOB_USD'),
        ('partner', 'CO'),
        ('start', '?startPeriod=2022')]
series = '.'.join([i[1] for i in param[1:5]])


key = f'CompactData/{param[0][1]}/{series}{param[-1][1]}'


r = requests.get(f'{url}{key}').json()
data = r['CompactData']['DataSet']['Series']


data_list = [[obs.get('@TIME_PERIOD'), obs.get('@OBS_VALUE')]
   for obs in data['Obs']]
df2 = pandas.DataFrame(data_list, columns = ["Date", "Value (Millions USD)"])


df2["Country"] = param[2][1]
df2["Partner"] = param[4][1]


# #combining both data sets
# df = pandas.concat([df, df2])


df2.to_csv(os.path.join(cwd, "checkmate.csv"), header = True)





