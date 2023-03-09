import fromcomtradepkg
import pandas
import my_input
import os

class Comtrade:

    cwd = os.getcwd()
    # cwd = os.path.dirname(cwd) # gets parent of cwd, only use if not running in RStudio
    directory = os.path.join(cwd, "data")
    subscription_key = "9be8b0a6438a4940bd592c691bb2c4ca"

    def __init__(self):
        pass

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
            mydf = fromcomtradepkg.getFinalData(Comtrade.subscription_key, typeCode='C', freqCode=freq, clCode='HS', period=date,
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
        input_list = my_input.get_input(specs, None)
        Comtrade.all(input_list[0], input_list[1])
        print("All done! Check the data folder to see your new files.\n")

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
            mydf = fromcomtradepkg.getFinalData(Comtrade.subscription_key, typeCode='C', freqCode=freq, clCode='HS', period=date,
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
        input_list = my_input.get_input(specs, None)
        Comtrade.total(input_list[0], input_list[1])
        print("All done! Check the data folder to see your new files.\n")

# putting it all together
# def main():
#     comtrade_obj = Comtrade()
#     comtrade_obj.get_all_exports()
#     comtrade_obj.get_total_exports()

# if __name__ == "__main__":
#     main()
