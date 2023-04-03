# Economic Sanctions
###### Research @ Duke University - Nicholas School of the Environment | In collaboration with Morad Bali
Built upon a Python package created for this project ([export_ease](https://pypi.org/project/export-ease/)) and an R package that call JSON RESTful API to gather macroeconomic data, this program offers a streamlined interface through which you can request and analyze vast amounts of macroeconomic data from sources including UN Comtrade, International Monetary Fund (IMF), and World Bank. Below is a step-by-step guide detailing effective use of this program.
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
* Now, run the next code chunk to install/import the Python packages that the program needs in order to work properly. As the code executes, RStudio will likely ask you to install a miniconda environment--go ahead and install it, as it'll enable you to run the code smoothly from here on out. 
* Every time you open RStudio, be sure to run ```git pull``` in the terminal--this will update your local clone of the project with the most up-to-date changes.
## Running the Program
### Comtrade
* This part of the program utilizes the [comtradeapicall](https://pypi.org/project/comtradeapicall/) Python package to implement additional functionality.
* Start by sourcing ```comtrade.py``` and creating an object of the Comtrade class (defined in ```comtrade.py```) so that you can call the class' corresponding methods.
* Now, you can call either the ```get_total_exports``` function or the ```get_all_exports``` function, or both:
  * ```get_all_exports```: writes csv file containing export data for all available country pairs
  * ```get_total_exports```: writes csv file containing total-export (exports to world) data for all available reporters
* When you run these functions, you'll need to enter the parameters for your query in the console. The program will ask you for the input that the query requires. Once the program's finished running, it'll output the names of the files that were just created.
* After you've queried the data you want, run the next code chunk to compile ```clean_comtrade```, the function that will clean up the data you gathered in the previous step and write the resulting data frame to csv and Excel files (located in ```data```). It takes as input the file to be cleaned (i.e., the file names printed in the console), minus the extension (the cleaning functions will take care of that).
* Update the following code chunk to represent the new files you'd like to clean and the names of the data frames you'd like to save that data to.
* Then, run the cleaning functions and examine the cleaned data frame/files.
### IMF
* Repeat the steps outlined in the Comtrade section above, as the code to get IMF data is almost identical in structure to Comtrade's. 
* The only difference is the input required to make the query, but there's no need to worry about accidentally typing the wrong input, as the program will ensure the input is valid before making the API call.
* Functions with which to query data:
  * ```get_total_exports```: same as Comtrade's get_total_exports method
  * ```get_reporter_exports```: writes csv file containing value exports from reporter provided in console input to all its partners 
### World Bank
* Unlike the previous two sources, the code for getting World Bank data does not make any API calls (at least not directly)--all functionality is provided by the [wbstats](https://github.com/gshs-ornl/wbstats) R package.
* This section is also similar in structure to the previous two. Begin by compiling ```get_wb```, which both gets and cleans the data requested.
* Then, make the actual function call in the next code chunk, and provide two arguments, the first being the number of years for which to gather data relative to the current year (e.g., 5 will retrieve the data published in the most recent 5 years) and the second being the data frame to return: the two valid inputs are "gdp" and "total exports," which will return the corresponding data frame. 
  * ```get_wb```: writes two csv and Excel files, one containing GDP and the other total-export data (both include every possible reporter)
* Note: No matter which data frame you return, both will be written to csv and Excel files. If you'd like to view both data frames, run ```get_wb``` twice, calling it once with "gdp" as an argument and then again with "total exports" as an argument.
### Other Notes
* ```Ctrl-shift-c```/```cmd-shift-c``` uncomments/comments out a block/line of code; commented code will not run. (I often use this with the viewing function to only view the data frames when needed.)
* The cleaning functions for Comtrade and IMF (```clean_comtrade``` and ```clean_imf```, respectively) will not work if you've already cleaned the files that you're passing into these functions.
* You must update the file names when cleaning new Comtrade and IMF data. When you run the Python modules to get new data, the new file names will be printed in the console. These are the file names you should replace each file name with. Though not necessary, it'd likely be beneficial to also update the names of the data frames whenever you run new queries.
* Comtrade functions will retrieve data for the given year only, while IMF functions will retrieve data starting at the given year and ending with the most recently published data.
* The ```get_reporter_exports``` function for IMF has a quirk that occurs when the user requests a query for annual data starting at a year within 3 years of the current year. In this case, the function will "override" the user's indicated year and instead make the starting year 3 years less than the current year--I had to add this padding in order to work around the varying structures of the JSON file returned by the IMF API. This has no serious implications, as it still gets all the data you requested (and then some).
### Summary
* Reporter-to-all-Partners Export Sources: Comtrade (all country pairs) and IMF (one country pair @ a time)
* Total-Export Sources: Comtrade (all reporters), IMF (all reporters), and World Bank (all reporters)
* GDP Source: World Bank (all reporters)
* All data is expressed in USD, and most data is available in both monthly and annual quantities, with World Bank being the only source that supports annual data only.
* Get new data by running the get methods. The only get function that requires any arguments is ```get_wb```, which requires the number of years to gather data for, followed by the name of the data frame to return ("gdp" or "exports" are the two valid inputs).
* Clean data currently in ```data```(that hasn't yet been cleaned) with the clean functions (only for Comtrade and IMF, as the cleaning of World Bank data is built into the ```get_wb``` function). All clean functions require only one argument: the file name (minus the extension) to clean.
* When getting and cleaning new data, be sure to update file names to clean and the names of data frames to save the newly cleaned files to.
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
