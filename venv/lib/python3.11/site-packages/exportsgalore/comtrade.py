import comtradeapicall
import datetime
import pandas
import os

class Comtrade:

    cwd = os.getcwd()
    parent = os.path.dirname(cwd)
    directory = os.path.join(parent, "data")
    subscription_key = "9be8b0a6438a4940bd592c691bb2c4ca"

    def __init__(self):
        pass

    # function to get valid input for reporter, partner, and start year
    @classmethod
    def get_input(cls, input_list: list, input_dict: dict):
        def get_year():
            while True:
                try:
                    year = int(input("Enter a year between 1970 and the current year, inclusive, for which you'd like to gather data. \n"))
                except ValueError:
                    print("Invalid input.")
                else: 
                    curr_year = int(datetime.date.today().year)
                    if year < 1970 or year > curr_year:
                        print("Invalid input.")
                        continue
                    else:
                        break
            print()
            return year
        def get_freq():
            freqs = {"A", "B", "M"}
            while True:
                freq = input("Enter the frequency of the data you'd like to query: M for monthly, A for annual, and B for both. \n")
                if freq in freqs:
                    break
                else: 
                    print("Invalid input.")
            print()
            return freq
        output = []
        for i in range(len(input_list)):
            if input_list[i] == "year":
                item = get_year()
            else:
                item = get_freq()
            output.append(item)
        return output

    # helper function for get_all_exports
    @classmethod
    def all(cls, freq, year):
        if freq == "B":
            Comtrade.all("A", year)
            Comtrade.all("M", year)
        else:
            date = year
            if freq == 'M':
                date = f'{year}01,{year}02,{year}03,{year}04,{year}05,{year}06,{year}07,{year}08,{year}09,{year}10,{year}11,{year}12'
            mydf = comtradeapicall.getFinalData(Comtrade.subscription_key, typeCode='C', freqCode=freq, clCode='HS', period=date,
                                                reporterCode=None, cmdCode='TOTAL', flowCode='X', partnerCode=None,
                                                partner2Code=None,
                                                customsCode=None, motCode=None, maxRecords=None, format_output='JSON',
                                                aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True)
            df = pandas.DataFrame(mydf)
            file_name = f'comtrade_all_exports_{year}{freq}.csv'
            print(f'Writing {file_name}....')
            df.to_csv(os.path.join(Comtrade.directory, file_name))

    # function to get all available country-pair export data
    def get_all_exports(self):
        specs = ["freq", "year"]
        input_list = Comtrade.get_input(specs, None)
        Comtrade.all(input_list[0], input_list[1])

    # helper function for get_total_exports
    @classmethod
    def total(cls, freq, year):
        if freq == "B":
            Comtrade.total("A", year)
            Comtrade.total("M", year)
        else:
            date = year
            if freq == 'M':
                date = f'{year}01,{year}02,{year}03,{year}04,{year}05,{year}06,{year}07,{year}08,{year}09,{year}10,{year}11,{year}12'
            mydf = comtradeapicall.getFinalData(Comtrade.subscription_key, typeCode='C', freqCode=freq, clCode='HS', period=date,
                                                reporterCode=None, cmdCode='TOTAL', flowCode='X', partnerCode=0,
                                                partner2Code=None,
                                                customsCode=None, motCode=None, maxRecords=None, format_output='JSON',
                                                aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True)
            df = pandas.DataFrame(mydf)
            file_name = f'comtrade_total_exports_{year}{freq}.csv'
            print(f'Writing {file_name}....')
            df.to_csv(os.path.join(Comtrade.directory, file_name))

    # function to get all available total-export data (i.e., partner is world)
    def get_total_exports(self):
        specs = ["freq", "year"]
        input_list = Comtrade.get_input(specs, None)
        Comtrade.total(input_list[0], input_list[1])
