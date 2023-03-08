import fromcomtradepkg
import pandas
import my_input
import os

directory = os.getcwd() + '/data'
subscription_key = '9be8b0a6438a4940bd592c691bb2c4ca'

# function to get all available country-pair export data
def get_all_exports():
    def all(freq, year):
        if freq == "B":
            all("A", year)
            all("M", year)
        else:
            date = year
            if freq == 'M':
                date = f'{year}01,{year}02,{year}03,{year}04,{year}05,{year}06,{year}07,{year}08,{year}09,{year}10,{year}11,{year}12'
            mydf = fromcomtradepkg.getFinalData(subscription_key, typeCode='C', freqCode=freq, clCode='HS', period=date,
                                                reporterCode=None, cmdCode='TOTAL', flowCode='X', partnerCode=None,
                                                partner2Code=None,
                                                customsCode=None, motCode=None, maxRecords=None, format_output='JSON',
                                                aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True)
            df = pandas.DataFrame(mydf)
            file_name = f'comtrade_{year}{freq}.csv'
            df.to_csv(os.path.join(directory, file_name))
    specs = ["freq", "year"]
    input_list = my_input.get_input(specs, None)
    all(input_list[0], input_list[1])
    print("All done! Check the data folder to see your new files.\n")

# function to get all available total-export data (i.e., partner is world)
def get_total_exports():
    def total(freq, year):
        if freq == "B":
            total("A", year)
            total("M", year)
        else:
            date = year
            if freq == 'M':
                date = f'{year}01,{year}02,{year}03,{year}04,{year}05,{year}06,{year}07,{year}08,{year}09,{year}10,{year}11,{year}12'
            mydf = fromcomtradepkg.getFinalData(subscription_key, typeCode='C', freqCode=freq, clCode='HS', period=date,
                                                reporterCode=None, cmdCode='TOTAL', flowCode='X', partnerCode=0,
                                                partner2Code=None,
                                                customsCode=None, motCode=None, maxRecords=None, format_output='JSON',
                                                aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True)
            df = pandas.DataFrame(mydf)
            file_name = f'comtrade_total_{year}{freq}.csv'
            df.to_csv(os.path.join(directory, file_name))
    specs = ["freq", "year"]
    input_list = my_input.get_input(specs, None)
    total(input_list[0], input_list[1])
    print("All done! Check the data folder to see your new files.\n")

# putting it all together
def main():
    get_all_exports()
    get_total_exports()

if __name__ == "__main__":
    main()

