# Economic Sanctions
###### Research @ Duke University - Nicholas School of the Environment | In collaboration with Morad Bali
Built upon a Python package ([export_ease](https://pypi.org/project/export-ease/)) that calls JSON RESTful API to gather macroeconomic data, this program offers a streamlined interface through which you can request and analyze vast amounts of macroeconomic data from sources including UN Comtrade, International Monetary Fund (IMF), and World Bank. Below is a step-by-step guide detailing effective use of this program.
## Setup
* Clone the repository by clicking on ```Code``` and copying the SSH link.
* Create a new project by clicking on the 3D box in the upper-left corner. Click ```Version Control``` and then ```Git```, and then paste the link that you copied.
* Navigate to the ```src``` folder and open ```Sanctions.qmd```; this is the only file that you'll need to have open in order to run the program (though you may also want to view a csv/xlsx file in the ```data``` folder--you can do this by clicking on said file).
  * Side note: If you want to view an Excel file, it's easiest to download it from this repository directly.
* Run the first code chunk to install all the necessary packages. You can delete this chunk after installation. After saving your changes locally, you can commit and push your changes to GitHub by running the following commands in the terminal:
```
git add .
git commit -m "your message here"
git push
```
* Load the packages you just installed by running the second code chunk.
* Now, run the next code chunk to install/import the Python packages that the program needs in order to work properly. 
* Every time you open RStudio, be sure to run ```git pull``` in the terminal--this will update your local clone of the project with the most up-to-date changes.
## Running the Program
* Simply specify the year for which you'd like to gather data by editing the year variable in the first code chunk of the ```Viewing + Getting Data``` section. When you run ```final <- everything(year)``` (within the same code chunk), the functions provided will query, clean, merge, convert frequency, and calculate beta for all available countries.
## Documentation
### Comtrade
This part of the program utilizes the comtradeapicall Python package to implement additional functionality.
To query export data from Comtrade, you can use the following methods:
  * ```get_all_exports```: writes csv file containing export data for all available country pairs (i.e., exports from each reportner to all its partners)
  * ```get_total_exports```: writes csv file containing total-export (exports to world) data for all available reporters

When you run these functions, you'll need to enter the criteria for your query. Both of these functions require two arguments, the first being the frequency ("A" for annual, "M" for monthly, or "B" for both) and the second being the year for which to gather data (e.g., 2021). Once the program's finished running, it'll output the names of the files that were just created.
### IMF
Functions with which to query data:
  * ```get_reporter_exports```: writes csv file containing value exports from reporter provided in console input to all its partners
  * ```get_total_exports```: same as Comtrade's ```get_total_exports``` method

The code to get IMF data is almost identical in structure to Comtrade's. The only difference is the arguments for ```get_reporter_exports``` (```get_total_exports``` is the same for both Comtrade and IMF): the first argument is the name of the reporting country for which you'd like to gather (e.g., "France"), followed by the frequency and year (in the same format as Comtrade's).
If you input an incorrect country name for ```get_reporter_exports```, you can check country_codes.csv to see valid country names (this file is written by the program when you run ```get_reporter_exports```).
### World Bank
* Unlike the previous two sources, the code for getting World Bank data does not make any API calls (at least not directly)--all functionality is provided by the [wbstats](https://github.com/gshs-ornl/wbstats) R package.
  * ```get_wb```: writes two csv and Excel files, one containing GDP and the other total-export data (both include every possible reporter) and outputs the names of the files written (in the console)
* Note: No matter which data frame you return, both will be written to csv and Excel files. If you'd like to view both data frames, either run ```get_wb``` twice, changing the data frame-to-return parameter each time, or run ```get_wb``` once and then load the data frame that wasn't returned with ```df <- read_csv(file.path(dirname(getwd()), "data", file_name.csv))```.
## Other Notes
* All data is expressed in USD, and most data is available in both monthly and annual quantities, with World Bank being the only source that supports annual data only. None of the data is seasonally adjusted, nor is it inflation adjusted.
* Comtrade functions will retrieve data for the given year only, while IMF functions will retrieve data starting at the given year and ending with the most recently published data.
* The ```get_reporter_exports``` function for IMF has a quirk that occurs when the user requests a query for annual data starting at a year within 3 years of the current year. In this case, the function will "override" the user's indicated year and instead make the starting year 3 years less than the current year--I had to add this padding in order to work around the varying structures of the JSON file returned by the IMF API. This has no serious implications, as it still gets all the data you requested (and then some).
* ```Ctrl-shift-c```/```cmd-shift-c``` uncomments/comments out a block/line of code; commented code will not run. (I often use this with the viewing function to only view the data frames when needed.)
### Summary
* Reporter-to-all-Partners Export Sources: Comtrade (all country pairs) and IMF (one country pair @ a time)
* Total-Export Sources: Comtrade (all reporters), IMF (all reporters), and World Bank (all reporters)
* GDP Source: World Bank (all reporters)
## Resources
### Comtrade
* [New User Guide](https://unstats.un.org/wiki/display/comtrade/New+Comtrade+User+Guide#NewComtradeUserGuide-Tariffline)
* [Python Package Documentation](https://pypi.org/project/comtradeapicall/)
* [API Interface](https://comtradedeveloper.un.org/signin?returnUrl=%2Fapi-details#api=comtrade-v1&operation=get-get)
  * Requires an account and a subscription key
  * Allows you to determine what call you need to make given specific parameters and see if a call if valid or not, but doesn't allow you to download data directly from this page
### IMF
* API
  * [Documentation](https://datahelp.imf.org/knowledgebase/articles/667681-json-restful-web-service)
  * [Guide](http://www.bd-econ.com/imfapi1.html)
  * [Examples](https://github.com/bdecon/econ_data/blob/master/APIs/IMF.ipynb)
* Bulk Query
  * [Guide](https://datahelp.imf.org/knowledgebase/articles/493639-export-data-how-to-bulk-download)
  * [Webpage](https://data.imf.org/?sk=388DFA60-1D26-4ADE-B505-A05A558D9A42&sId=1479329334655)
    * Allows you to manually get export data for every possible country-pair (not possible through IMF's API)
### World Bank
* [R Package Documentation](https://cran.r-project.org/web/packages/wbstats/wbstats.pdf)
* [Examples](https://rdrr.io/cran/wbstats/man/wb_data.html)
* [More Examples](https://cran.r-project.org/web/packages/wbstats/vignettes/wbstats.html#:~:text=The%20wbstats%20R%2Dpackage%20allows,with%20realtime%20access%20to%20the)
* [More More Examples](https://jesse.netlify.app/2018/01/08/getting-started-with-wbstats-a-world-bank-r-package/)
