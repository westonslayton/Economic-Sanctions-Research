# function to get valid input for reporter, partner, and start year
def get_input(input_list: list, input_dict: dict):
    def get_year():
        while True:
            try:
                year = int(input("Enter a year between 1970 and the current year, inclusive, at which to start gathering data.\n"))
            except ValueError:
                print("Invalid input.")
            else: 
                break
        print()
        return year
    def get_country(input_dict):
        while True:
            count = input("Enter the name of the country.\n")
            if count in input_dict:
                break
            else:
                print("Invalid input. See imf_country_codes.csv for valid country name.")
        print()
        return count
    def get_freq():
        freqs = {"A", "B", "M"}
        while True:
            freq = input("Enter the frequency of the data you'd like to query: M for monthly, A for annual, and B for both.\n")
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
        elif input_list[i] == "country":
            item = get_country(input_dict)
        else:
            item = get_freq()
        output.append(item)
    return output