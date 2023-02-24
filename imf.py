import requests
import os
import pandas as pd

#root url
url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'

#part of url that accesses exports from country to partner beginning at start date (yr)
param = [('dataset', 'DOT'),
         ('freq', 'M'),
         ('country', 'ZM'),
         ('series', 'TXG_FOB_USD'),
         ('partner', 'ZW'),
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
df = pd.DataFrame(data_list, columns = ["Date", "Value (Millions USD)"])

#adding country + partner columns to data frame
df["Country"] = param[2][1]
df["Partner"] = param[4][1]

#save cleaned dataframe as a csv file and save to data folder
#df.to_csv('export_ex.csv', header = True)
cwd = os.getcwd() + "/data"
df.to_csv(os.path.join(cwd, "export_ex.csv"), header = True)



#second data set
param = [('dataset', 'DOT'),
         ('freq', 'M'),
         ('country', 'IT'),
         ('series', 'TXG_FOB_USD'),
         ('partner', 'FR'),
         ('start', '?startPeriod=2022')]
series = '.'.join([i[1] for i in param[1:5]])

key = f'CompactData/{param[0][1]}/{series}{param[-1][1]}'

r = requests.get(f'{url}{key}').json()
data = r['CompactData']['DataSet']['Series']

data_list = [[obs.get('@TIME_PERIOD'), obs.get('@OBS_VALUE')]
    for obs in data['Obs']]
df2 = pd.DataFrame(data_list, columns = ["Date", "Value (Millions USD)"])

df2["Country"] = param[2][1]
df2["Partner"] = param[4][1]

#combining both data sets
df = pd.concat([df, df2])

cwd = os.getcwd() + "/data"
df.to_csv(os.path.join(cwd, "export_ex2.csv"), header = True)





#getting list of country codes
key = 'DataStructure/DOT'  # Method/series
dimension_list = requests.get(f'{url}{key}').json()\
            ['Structure']['KeyFamilies']['KeyFamily']\
            ['Components']['Dimension']

key = f"CodeList/{dimension_list[1]['@codelist']}"
code_list = requests.get(f'{url}{key}').json()\
	    ['Structure']['CodeLists']['CodeList']['Code']
#for code in code_list:
    #print(f"{code['Description']['#text']}: {code['@value']}")

#loop to get exports for every country pair
big_df = pd.DataFrame()
for country in code_list:
    for partner in code_list:
        if country['@value'] != partner['@value']:
            param = [('dataset', 'DOT'),
            ('freq', 'M'),
            ('country', country['@value']),
            ('series', 'TXG_FOB_USD'),
            ('partner', partner['@value']),
            ('start', '?startPeriod=2022')]
            series = '.'.join([i[1] for i in param[1:5]])
            key = f'CompactData/{param[0][1]}/{series}{param[-1][1]}'
            #r = requests.get(f'{url}{key}').json()
            #data = r['CompactData']['DataSet']['Series']
            #data_list = [[obs.get('@TIME_PERIOD'), obs.get('@OBS_VALUE')]
                #for obs in data['Obs']]
            #df = pd.DataFrame(data_list, columns = ["Date", "Value (Millions USD)"])
            data = requests.get(f'{url}{key}').json()
            df = pd.DataFrame({[[obs.get('@TIME_PERIOD'), obs.get('@OBS_VALUE')]
                    for obs in s['Obs']]
                for s in data['CompactData']['DataSet']['Series']})
            df["Country"] = country['Description']['#text']
            df["Partner"] = partner['Description']['#text']
            big_df = pd.concat(big_df, df)



#testing new way of getting dfs; works indiv but in loop???       
url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/DOT/M.US.TXG_FOB_USD.W00.?startPeriod=2022'
data = requests.get(url).json()
usexp = pd.DataFrame(data['CompactData']['DataSet']['Series']['Obs'])
usexp.columns = ['date','value (millions USD)']
usexp["country"] = "US"
usexp["partner"] = "WOO"
usexp.to_csv(os.path.join(cwd, "us_exp.csv"), header = True)