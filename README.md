# Economic Sanctions
###### Research @ Duke University - Nicholas School of the Environment | In collaboration with Morad Bali

## Setup
* Clone the repository by clicking on the code button and copying the SSH link.
* Create a new project by clicking on the 3D box in the upper-left corner. Click version control and then git, and then paste the link that you copied.
* Open the Sanctions.qmd document in the src folder; this is the only file that you'll need to have open in order to run the program (though you may also want to view the csv/xlsx files in the data folder--you can do this by clicking on the file).
* Run the first code chunk to install all the necessary packages. You can delete this chunk after installation. After saving your changes locally, you can commit and push your changes to GitHub by running the following commands in the terminal:
 * git add .
  * git commit -m "your message here"
  * git push
* When installing/importing the Python packages, RStudio will likely ask you to install a miniconda environment--go ahead and install it, as it'll enable you to run the code smoothly from here on out.

## Running the Program
* The cleaning functions for Comtrade and IMF (clean_comtrade and clean_imf, respectively) will not work if you've already cleaned the files that you're passing into these functions.
* You must update the file names when cleaning new Comtrade and IMF data. When you run the Python modules to get new data, the new file names will be printed in the console. These are the file names you should replace each file name with (minus the .csv extension--the cleaning functions will take care of that). Though not mandatory, it'd likely be beneficial to also update the names of the data frames whenever you run new queries.

## Documentation
### Comtrade
*
### IMF
*
### World Bank
*
## Resources
### Comtrade
*
### IMF
*
### World Bank
*
