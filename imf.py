import requests
import os
import pandas as pd

#root url
url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'

#part of url that accesses exports from country to partner beginning at start date (yr)
param = [('dataset', 'DOT'),
         ('freq', 'M'),
         ('country', 'IT'),
         ('series', 'TXG_FOB_USD'),
         ('partner', 'FR'),
         ('start', '?startPeriod=2022')]
series = '.'.join([i[1] for i in param[1:5]])

#form rest of url after root
key = f'CompactData/{param[0][1]}/{series}{param[-1][1]}'

#combine API url with key specific to data request
r = requests.get(f'{url}{key}').json()

#data portion of results
data = r['CompactData']['DataSet']['Series']

#create pandas data frame from the observations
data_list = [[obs.get('@TIME_PERIOD'), obs.get('@OBS_VALUE')]
             for obs in data['Obs']]
df = pd.DataFrame(data_list, columns=["date", "value (USD MM)"])

#adding country + partner columns to data frame
df["Country"] = param[2][1]
df["Partner"] = param[4][1]

#save cleaned dataframe as a csv file and save to data folder
#df.to_csv('export_ex.csv', header=True)
cwd = os.getcwd() + "/data"
df.to_csv(os.path.join(cwd, "export_ex.csv"), header = True)
