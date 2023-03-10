# Economic Sanctions
###### Research @ Duke University - Nicholas School of the Environment | In collaboration with Morad Bali

## Setup
* Clone the repository by clicking on the code button and copying the SSH link.
* Create a new project by clicking on the 3D box in the upper-left corner. Click version control and then git, and then paste the link that you copied.
* Open the Sanctions.qmd document in the src folder; this is the only file that you'll need to have open in order to run the program (though you may also want to view a csv/xlsx file in the data folder--you can do this by clicking on said file).
  * Side note: If you want to view an Excel file, it's easiest to download it from this repo directly.
* Run the first code chunk to install all the necessary packages. You can delete this chunk after installation. After saving your changes locally, you can commit and push your changes to GitHub by running the following commands in the terminal:
  * git add .
  * git commit -m "your message here"
  * git push
* Load the packages you just installed by running the second code chunk.
* Now, run the next code chunk to install/import the Python packages that the program needs in order to work properly. As the code executes, RStudio will likely ask you to install a miniconda environment--go ahead and install it, as it'll enable you to run the code smoothly from here on out. 
* Every time you open RStudio, be sure to run "git pull" in the terminal--this will update your local clone of the project with the most up-to-date changes.

## Running the Program
### Comtrade
* Start by sourcing the comtrade.py file and creating an object of the Comtrade class defined in comtrade.py so that you can call comtrade.py's methods.
* Now, you can call either the get_total_exports function or the get_all_exports_function, or both:
  * get_all_exports: writes csv file to data folder containing export data for all available country pairs
  * get_total_exports: writes csv file to data folder containing total-export (exports to world) data for all available reporters
* When you run these functions, you'll need to enter the parameters for your query in the console. The program will ask you for the input that the query requires.
### Other Notes
* The cleaning functions for Comtrade and IMF (clean_comtrade and clean_imf, respectively) will not work if you've already cleaned the files that you're passing into these functions.
* You must update the file names when cleaning new Comtrade and IMF data. When you run the Python modules to get new data, the new file names will be printed in the console. These are the file names you should replace each file name with (minus the .csv extension--the cleaning functions will take care of that). Though not mandatory, it'd likely be beneficial to also update the names of the data frames whenever you run new queries.
* Comtrade functions will retrieve data for the given year only, while IMF functions will retrieve data starting at the given year and ending with the most recently published data.
* The get_reporter_exports function for IMF has a quirk that occurs when the user requests a query for annual data starting at a year within 3 years of the current year. In this case, the function will "override" the user's indicated year and instead make the starting year 3 years less than the current year--I had to add this padding in order to work around the varying structures of the JSON file returned by the IMF API. This has no serious implications, as it still gets all the data you requested.
### Summary
* All-partner export sources: Comtrade (all country pairs) and IMF (one country pair @ a time)
* Total-export sources: Comtrade (all reporters), IMF (all reporters), and World Bank (all reporters)
* GDP source: World Bank (all reporters)
* All data is expressed in USD, and most data is available in both monthly and annual quantities, with World Bank being the only source that supports annual data only.
* Get new data by running the get methods.
* Clean data currently in the data folder with the clean methods (only for Comtrade and IMF, as the cleaning of World Bank data is built into the get_wb function.
* When getting and cleaning new data, be sure to update file names to clean and the names of data frames to save the newly cleaned files to.
* 

## Resources
### Comtrade
*
### IMF
* Bulk query: data is in millions USD
### World Bank
*
